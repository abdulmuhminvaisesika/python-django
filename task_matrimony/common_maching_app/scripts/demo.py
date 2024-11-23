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



# List of education levels commonly pursued in India
def create_option_education():
    education_levels = [
        'Primary School', 'Middle School', 'High School', 'Higher Secondary',
        'Diploma', 'Bachelor of Arts', 'Bachelor of Science', 'Bachelor of Commerce',
        'Bachelor of Engineering', 'Bachelor of Technology', 'Master of Arts',
        'Master of Science', 'Master of Commerce', 'Master of Engineering',
        'Master of Technology', 'Doctor of Philosophy (PhD)', 'Medical Doctor (MD)',
        'Bachelor of Medicine, Bachelor of Surgery (MBBS)', 'Bachelor of Education',
        'Master of Education'
    ]

    # Loop through the education levels and create a Common_Matching entry for each
    for i, level in enumerate(education_levels, start=1):
        # Format code like ED001, ED002, etc.
        code = f"ED{str(i).zfill(3)}"
        
        # Check if education level already exists to avoid duplicates
        if not Common_Matching.objects.filter(type='education', code=code).exists():
            Common_Matching.objects.create(
                type='education',
                code=code,
                name=level,
                display_name=level
            )

    print("Education options created successfully!")



# List of common professions in India
def create_option_profession():
    professions = [
        'Software Engineer', 'Doctor', 'Teacher', 'Lawyer', 'Accountant',
        'Civil Engineer', 'Mechanical Engineer', 'Pharmacist', 'Business Analyst', 'Artist',
        'Scientist', 'Architect', 'Nurse', 'Dentist', 'Data Scientist',
        'Chef', 'Journalist', 'Pilot', 'Banker', 'Police Officer'
    ]

    # Loop through the professions and create a Common_Matching entry for each
    for i, profession in enumerate(professions, start=1):
        # Format code like PR001, PR002, etc.
        code = f"PR{str(i).zfill(3)}"
        
        # Check if profession already exists to avoid duplicates
        if not Common_Matching.objects.filter(type='profession', code=code).exists():
            Common_Matching.objects.create(
                type='profession',
                code=code,
                name=profession,
                display_name=profession
            )

    print("Profession options created successfully!")



def create_option_location():
    # List of all states and union territories in India
    states_and_territories = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
        'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
        'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
        'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
        'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
        'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Andaman and Nicobar Islands',
        'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Lakshadweep',
        'Delhi', 'Puducherry', 'Ladakh', 'Jammu and Kashmir'
    ]

    # Loop through the list to create a Common_Matching entry for each state/territory
    for i, location in enumerate(states_and_territories, start=1):
        # Format code like ST001, ST002, etc.
        code = f"LC{str(i).zfill(3)}"
        
        # Check if the location already exists to avoid duplicates
        if not Common_Matching.objects.filter(type='location', code=code).exists():
            Common_Matching.objects.create(
                type='location',
                code=code,
                name=location,
                display_name=location
            )

    print("Location options for Indian states and territories created successfully!")





def create_option_caste():
    # List of common caste groups in India
    castes = [
        'General', 'OBC (Other Backward Class)', 'SC (Scheduled Caste)', 'ST (Scheduled Tribe)', 
        'Vaisya', 'Brahmin', 'Kshatriya', 'Vaishnav', 'Shudra', 'Kayastha', 
        'Rajput', 'Yadav', 'Maratha', 'Jat', 'Nair'
    ]

    # Loop through the list to create a Common_Matching entry for each caste
    for i, caste in enumerate(castes, start=1):
        # Format code like CA001, CA002, etc.
        code = f"CA{str(i).zfill(3)}"
        
        # Check if caste already exists to avoid duplicates
        if not Common_Matching.objects.filter(type='caste', code=code).exists():
            Common_Matching.objects.create(
                type='caste',
                code=code,
                name=caste,
                display_name=caste
            )

    print("Caste options created successfully!")


def create_height_options():
    # Define a list of height categories (in cm)
    height_categories = [
        (150, "150cm below"),
        (160, "160cm "),
        (170, "170cm "),
        (180, "180cm "),
        (190, "190cm "),
        (200, "200cm "),
        (210, "210cm "),
        (220, "220cm "),
        (230, "230cm above"),
    ]

    # Loop through the height categories and create entries in Common_Matching
    for index, (height, display_name) in enumerate(height_categories, start=1):
        # Generate the sequential code for each height option (e.g., HE001, HE002, etc.)
        code = f"HE{str(index).zfill(3)}"
        
        # Check if the height option already exists to avoid duplicates
        if not Common_Matching.objects.filter(type='height', code=code).exists():
            # Create a new Common_Matching entry for the height category
            Common_Matching.objects.create(
                type='height',
                code=code,  # Sequential code like HE001, HE002, etc.
                name=str(height),  # Name is the height in cm
                display_name=display_name  # Display name based on the height category
            )

    print("Height options created successfully!")


def delete_all_height_options():
    # Delete all Common_Matching entries where type is 'height'
    Common_Matching.objects.filter(type='height').delete()
    print("All height options have been deleted successfully!")






def create_weight_options():
    # Loop through weights from 30 to 100 inclusive
    for weight in range(30, 101):
        # Generate the sequential code for each weight option (e.g., WE001, WE002, etc.)
        code = f"WE{str(weight-29).zfill(3)}"  # Adjust code numbering, starting from WE001
        
        # Define the display name logic
        if weight == 30:
            display_name = "30 kg below"
        elif weight == 100:
            display_name = "100 above"
        else:
            display_name = f"{weight} kg"
        
        # Check if the weight option already exists to avoid duplicates
        if not Common_Matching.objects.filter(type='weight', code=code).exists():
            # Create a new Common_Matching entry for the weight category
            Common_Matching.objects.create(
                type='weight',
                code=code,  # Sequential code like WE001, WE002, etc.
                name=str(weight),  # Name is the weight in kg
                display_name=display_name  # Display name based on the weight category
            )

    print("Weight options created successfully!")


def delete_income_options():
    # Delete all income options in the Common_Matching table
    deleted_count, _ = Common_Matching.objects.filter(type='weight').delete()

    print(f"Deleted {deleted_count} income options successfully.")



def create_income_options():
    # Generate income options from 1LPA to 30LPA with increments of 0.5LPA
    income_values = [i * 0.5 for i in range(2, 61)]  # This will create values from 1.0, 1.5, 2.0, ..., 30.0

    # Loop through the generated income values and create corresponding entries
    for index, income in enumerate(income_values, start=1):
        # Format the code as IN001, IN002, ..., IN060
        code = f"IN{str(index).zfill(3)}"
        
        # Check if income already exists to avoid duplicates
        if not Common_Matching.objects.filter(type='income', code=code).exists():
            display_name = f"{income}LPA"
            # Create the income option in Common_Matching
            Common_Matching.objects.create(
                type='income',
                code=code,
                name=str(income),
                display_name=display_name
            )

    print("Income options created successfully!")



def add_languages():
    # List of languages commonly spoken in India
    languages = [
        ("Hindi", "language"),
        ("Bengali", "language"),
        ("Telugu", "language"),
        ("Marathi", "language"),
        ("Tamil", "language"),
        ("Urdu", "language"),
        ("Gujarati", "language"),
        ("Malayalam", "language"),
        ("Kannada", "language"),
        ("Odia", "language")
    ]
    
    # Loop through the languages and add them to the database
    for index, (language, lang_type) in enumerate(languages, start=1):
        # Generate the language code (LN001, LN002, etc.)
        code = f"LN{str(index).zfill(3)}"
        
        # Create a new language entry in the Common_Matching table
        Common_Matching.objects.create(
            type= lang_type,
            name=language,
            display_name=language,
            code=code  # The language code, e.g., LN001
        )
    
    print("Languages have been added successfully!")



def run():
    delete_income_options()
