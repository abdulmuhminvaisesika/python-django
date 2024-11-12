from common_maching_app.models import Common_Matching






# Function to create age options
def create_age_options():
    # Create age options from 19 to 80
    for age in range(19, 81):
        # Create a code for each age (e.g., "AG019" for 19, "AG020" for 20, etc.)
        code = f"AG{age:03}"
        
        # Create the age entry
        age_option, created = Common_Matching.objects.get_or_create(
            type='age',
            code=code,
            defaults={
                'name': f"{age}",
                'display_name': f"Age {age}"
            }
        )
        
        if created:
            print(f"Created age option: {age_option.name}")
        else:
            print(f"Age option {age_option.name} already exists.")



from common_maching_app.models import Common_Matching

# List of religions commonly followed in India
def create_option_religion():
    religions = [
        'Hinduism', 'Islam', 'Christianity', 'Sikhism', 'Buddhism',
        'Jainism', 'Zoroastrianism', 'Judaism', 'Baháʼí Faith', 'Animism'
    ]

    # Loop through the religions and create a Common_Matching entry for each
    for i, religion in enumerate(religions, start=1):
        # Format code like RE001, RE002, etc.
        code = f"RE{str(i).zfill(3)}"
        
        # Check if religion already exists to avoid duplicates
        if not Common_Matching.objects.filter(type='religion', code=code).exists():
            Common_Matching.objects.create(
                type='religion',
                code=code,
                name=religion,
                display_name=religion
            )

    print("Religion options created successfully!")


def run():
    create_option_religion()
