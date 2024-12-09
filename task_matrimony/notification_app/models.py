from django.db import models

# Create your models here.


class Notification_Table(models.Model):
    NOTIFICATION_CHOICES = (
        ('reminder', 'Reminder'),
        ('new_message', 'New_Message'),
        ('new_match', 'New_Match'),
        ('offer', 'Offer'),
        ('profile', 'Profile'),
        ('preferance', 'Preferance'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
        ('request', 'Request'),
        ('bulk', 'Bulk')
    )
    notification_id = models.AutoField(primary_key=True)
    notification_type = models.CharField(
        max_length=255,
        choices=NOTIFICATION_CHOICES,
        default='new_message'
    )
    notification_message = models.TextField()
    receiver_id = models.ForeignKey('user_app.CustomUser', related_name='notification_receiver', on_delete=models.CASCADE)
    notification_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notification_type
    
    