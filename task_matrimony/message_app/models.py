from django.db import models



# Create your models here.
class MessageTable(models.Model):
    message_id= models.AutoField(primary_key=True)
    sender_id = models.ForeignKey('user_app.CustomUser', related_name='sender', on_delete=models.CASCADE)
    receiver_id = models.ForeignKey('user_app.CustomUser', related_name='receiver', on_delete=models.CASCADE)
    message_content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message from {self.sender_id.username} to {self.receiver_id.username}"
    
   

    