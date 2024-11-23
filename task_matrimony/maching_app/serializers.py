from rest_framework import serializers


from .models import Matching
from user_profile_app.models import User_Profile_Table
from user_profile_app.serializers import UserProfileSerializer

class MatchingScoreModelSerializer(serializers.ModelSerializer):
    user2_profile = serializers.SerializerMethodField()
    created_on = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_on = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Matching
        fields = ['user1', 'user2', 'status', 'score', 'user2_profile','created_on', 'updated_on']
        read_only_fields = ['user1', 'user2', 'status','score']

    def get_user2_profile(self, obj):
        # Fetch the profile of user2 using User_Profile_Table
        try:
            profile = User_Profile_Table.objects.get(user=obj.user2)
            return UserProfileSerializer(profile).data  # Use the existing serializer
        except User_Profile_Table.DoesNotExist:
            return None  # Handle the case where no profile exists

