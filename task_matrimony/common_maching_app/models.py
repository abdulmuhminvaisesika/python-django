from django.db import models
from django.db.models import Max



# Create your models here.

class Common_Matching(models.Model):
    FIELD_TYPES = [
        ('age', 'Age'),
        ('gender', 'Gender'),
        ('weight', 'Weight'),
        ('height', 'Height'),
        ('religion', 'Religion'),
        ('caste', 'Caste'),
        ('income', 'Income'),
        ('profession', 'Profession'),
        ('education', 'Education'),
        ('marital_status', 'Marital Status'),
        ('language', 'Language'),
        ('location', 'Location'),
    ]
    
    type = models.CharField(max_length=20, choices=FIELD_TYPES)
    code = models.CharField(max_length=50, unique=True, blank=True)
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.display_name} ({self.type})"


    def save(self, *args, **kwargs):
        if not self.code:
            # Generate code prefix based on type
            prefix_map = {
                'age': 'AG',
                'gender': 'GN',
                'weight': 'WT',
                'height': 'HT',
                'religion': 'RE',
                'caste': 'CT',
                'income': 'IN',
                'profession': 'PR',
                'education': 'ED',
                'marital_status': 'MS',
                'language': 'LN',
                'location': 'LC',
            }
            prefix = prefix_map.get(self.type, 'XX')
            
            # Find the max code number for the current type
            last_code = Common_Matching.objects.filter(type=self.type).aggregate(Max('code'))['code__max']
            if last_code and last_code.startswith(prefix):
                # Extract numeric part of the code and increment it
                last_number = int(last_code[len(prefix):])
                new_number = last_number + 1
            else:
                # Start numbering from 1 if no previous code found
                new_number = 1

            # Format the new code with leading zeros (e.g., IN001)
            self.code = f"{prefix}{new_number:03}"
        
        super().save(*args, **kwargs)