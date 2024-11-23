from django.db import models
from django.core.exceptions import ValidationError


from user_profile_app.models import User_Profile_Table
class Matching(models.Model):
    STATUS_CHOICES = [
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
        ('Pending', 'Pending'),
    ]
    user1 = models.ForeignKey('user_app.CustomUser', on_delete=models.CASCADE, related_name="matches_initiated")
    user2 = models.ForeignKey('user_app.CustomUser', on_delete=models.CASCADE, related_name="matches_received")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    score = models.FloatField(default=0)  # Add score to calculate and store the matching score

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



    @property
    def user2_profile(self):
        """Fetch and return the profile of user2."""
        try:
            profile = User_Profile_Table.objects.get(user=self.user2)
            return profile  # Return the profile object
        except User_Profile_Table.DoesNotExist:
            return None
    def __str__(self):
        return f"Match: {self.user1} with {self.user2} - {self.status} (Score: {self.score})"
    
    