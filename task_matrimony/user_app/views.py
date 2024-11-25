from django.contrib.auth import authenticate, login
from datetime import timedelta


from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomUserSerializer
from .models import CustomUser
from notification_app.models import Notification_Table
from subcription_app.models import SubcriptionsForUser, SubcriptionTable


# Create your views here.

class UserCrudOperation(APIView):

    def get(self, request):
        try:
            users = CustomUser.objects.all()
            
            # Pagination
            paginator = PageNumberPagination()
            paginator.page_size = 5  # Set number of results per page
            paginated_users = paginator.paginate_queryset(users, request)
            
            serializer = CustomUserSerializer(paginated_users, many=True)
            return paginator.get_paginated_response(serializer.data)  # Paginated response

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


    # POST: Create a new user
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)

            # Handle subscription logic if subscription plan is provided
            subscription_plan = user.subcription_plan
            if subscription_plan:
                try:
                    # Retrieve subscription details from SubcriptionTable
                    subscription_details = SubcriptionTable.objects.get(subcription_type=subscription_plan)

                    # Create entry in SubcriptionsForUser
                    SubcriptionsForUser.objects.create(
                        user_id=user,
                        subcription_type=subscription_details,
                        subcription_price=subscription_details.subcription_price,
                        subcription_duration=subscription_details.subcription_duration,
                        subcription_started_at=user.join_date,
                        subcription_ending_at = user.join_date + timedelta(days=subscription_details.subcription_duration)

                    )
                except SubcriptionTable.DoesNotExist:
                    return Response({"error": "Invalid subscription plan"}, status=status.HTTP_400_BAD_REQUEST)
                
                Notification_Table.objects.create(
                    sender_id_id= user.user_id,
                    receiver_id_id=user.user_id,  # Notification for this user
                    notification_type="",
                    notification_message=f"🎉 Your subscription plan '{subscription_plan}' is officially activated! 💍 Get ready to meet your perfect match! 💖 You've got {subscription_plan.subcription_duration} days of adventure ahead. Enjoy every moment! 😘",
                    is_read=False
                )
                
                


    
            # Query all existing users except the newly created user
            all_users = CustomUser.objects.exclude(user_id=user.user_id)
            # Create a notification for all other users
            for existing_user in all_users:
                Notification_Table.objects.create(
                    sender_id_id= user.user_id,
                    receiver_id_id=existing_user.user_id,  # Notification for this user
                    notification_type="riminder",
                    notification_message=f"A new user found! '{user.username}' has joined the platform.",
                    is_read=False)
                
                
            return Response({  
                "user": serializer.data,
                "token": token.key
                }, status=status.HTTP_201_CREATED)
        

            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCrudOperationByID(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):

        try:
            if request.user.user_id != user_id:
                return Response({"error": "You are not authorized to view this user's information."}, status=status.HTTP_403_FORBIDDEN)
        
            user = CustomUser.objects.get(user_id=user_id)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user_id):
        try:
            # Fetch the user
            user = CustomUser.objects.get(user_id=user_id)
            serializer = CustomUserSerializer(user, data=request.data)
            
            if serializer.is_valid():
                # Save user updates
                serializer.save()

                # Handle subscription logic if subscription plan is provided
                subscription_plan = user.subcription_plan
                if subscription_plan:
                    try:
                        # Retrieve subscription details from SubcriptionTable
                        subscription_details = SubcriptionTable.objects.get(subcription_type=subscription_plan)

                        # Update or create entry in SubcriptionsForUser
                        subscription, created = SubcriptionsForUser.objects.update_or_create(
                            user_id=user,
                            defaults={
                                "subcription_type": subscription_details,
                                "subcription_price": subscription_details.subcription_price,
                                "subcription_duration": subscription_details.subcription_duration,
                                "subcription_started_at": user.updated_on,
                                "subcription_ending_at": user.updated_on + timedelta(days=subscription_details.subcription_duration),
                                "subcription_active_status": True,
                            }
                        )

                        # Determine the notification message
                        if created:
                            # New subscription activated
                            notification_message = (
                                f"🎉 Your subscription plan '{subscription_plan}' is officially activated! 💍 Get ready to meet your perfect match! "
                                f"💖 You've got {subscription_details.subcription_duration} days of adventure ahead. Enjoy every moment! 😘"
                            )
                        else:
                            # Existing subscription reactivated
                            notification_message = (
                                f"🎉 Your subscription plan '{subscription_plan}' has been reactivated! You've got "
                                f"{subscription_details.subcription_duration} days left. Enjoy your experience! 😊"
                            )

                        # Create a notification for the user
                        Notification_Table.objects.create(
                            sender_id_id=user.user_id,
                            receiver_id_id=user.user_id,  # Notification for this user
                            notification_type="subscription",
                            notification_message=notification_message,
                            is_read=False
                        )

                    except SubcriptionTable.DoesNotExist:
                        return Response({"error": "Invalid subscription plan"}, status=status.HTTP_400_BAD_REQUEST)
                
                return Response(serializer.data, status=status.HTTP_200_OK)

            # Invalid data provided
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except CustomUser.DoesNotExist:
            # User not found
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
    def delete(self, request, user_id):
        try:
            user = CustomUser.objects.get(user_id=user_id)
            user.is_active = False
            user.save()
            return Response({"message": "User deleted successfully!"}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


# View for login (creates token)
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)  # Logs in the user and updates the `last_login` field

            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# View for logout (delete token)
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except (AttributeError, KeyError):
            return Response({"detail": "No active session to logout."}, status=status.HTTP_400_BAD_REQUEST)
