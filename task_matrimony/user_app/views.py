from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout


from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomUserSerializer
from .models import CustomUser



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
            return Response({
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCrudOperationByID(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user_id):
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = CustomUserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, user_id):
        try:
            user = CustomUser.objects.get(user_id=user_id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


# View for login (creates token)
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
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
