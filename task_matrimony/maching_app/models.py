from django.db import models
from django.core.exceptions import ValidationError

from rest_framework import status
from rest_framework.response import Response

class Matching(models.Model):
    user1 = models.ForeignKey('user_app.CustomUser', on_delete=models.CASCADE, related_name="matches_initiated")
    user2 = models.ForeignKey('user_app.CustomUser', on_delete=models.CASCADE, related_name="matches_received")
    status = models.CharField(max_length=20, choices=[('Rejected', 'Rejected'), ('Accepted', 'Accepted'), ('Pending', 'Pending')])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"Match: {self.user1} with {self.user2} - {self.status}"
