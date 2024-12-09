from django.db import models
from django.utils import timezone
from datetime import timedelta

class SubcriptionTable(models.Model):
    subcription_type = models.CharField(max_length=50, primary_key=True, unique=True)
    subcription_price = models.IntegerField(blank=True, null=True)
    subcription_duration = models.IntegerField(blank=True, null=True)  # Duration in days
    subcription_active_status = models.BooleanField(default=True)  # Active status
    

    def __str__(self):
        return self.subcription_type






class SubcriptionsForUser(models.Model):
    subcription_id = models.AutoField(primary_key=True)
    subcription_type = models.ForeignKey(SubcriptionTable, on_delete=models.CASCADE)
    subcription_price = models.IntegerField(null=True, blank=True)
    subcription_duration = models.IntegerField(null=True, blank=True)
    user_id = models.OneToOneField('user_app.CustomUser', on_delete=models.CASCADE)
    subcription_started_at = models.DateTimeField()
    subcription_ending_at = models.DateTimeField()
    subcription_active_status = models.BooleanField(default=True)



    def save(self, *args, **kwargs):

        """
        Automatically assign subscription price, duration, and calculate ending date.
        """
        if not self.subcription_started_at:
            self.subcription_started_at = timezone.now()

        # Retrieve subscription details from SubcriptionTable
        subcription_details = self.subcription_type
        if subcription_details:
            self.subcription_price = subcription_details.subcription_price
            self.subcription_duration = subcription_details.subcription_duration

            # Calculate the ending date based on the duration
            if self.subcription_duration:
                self.subcription_ending_at = self.subcription_started_at + timedelta(
                    days=self.subcription_duration
                )
                

        super().save(*args, **kwargs)

    
    def __str__(self):
        return f"{self.user_id} - {self.subcription_type}"
  


















# subcription_started_at = models.DateTimeField()  # Start date
    # subcription_ending_at = models.DateTimeField()  

    # def clean(self):
    #     """
    #     Validate subscription dates and other constraints.
    #     """
    #     if self.subcription_started_at and self.subcription_ending_at:
    #         if self.subcription_started_at >= self.subcription_ending_at:
    #             raise ValidationError("Ending date must be after the starting date.")

    # def save(self, *args, **kwargs):
    #     # Ensure validation is run
    #     self.clean()

    #     # Calculate subscription duration in days if dates are provided
    #     if self.subcription_started_at and self.subcription_ending_at:
    #         self.subcription_duration = (self.subcription_ending_at - self.subcription_started_at).days

    #         # Update active status based on current time
    #         current_time = timezone.now()
    #         self.subcription_active_status = self.subcription_started_at <= current_time <= self.subcription_ending_at

    #     # Call parent save method
    #     super().save(*args, **kwargs)