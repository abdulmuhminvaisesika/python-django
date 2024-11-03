import random
from school_app.models import School_Task
from department_app.models import Department_Task  # Adjust the import based on your app structure

def assign_random_departments_to_schools(num_departments_to_assign=2):
    schools = School_Task.objects.filter(is_active=True)
    departments = Department_Task.objects.filter(is_active=True)

    for school in schools:
        # Randomly select departments to assign
        selected_departments = random.sample(list(departments), k=min(num_departments_to_assign, len(departments)))

        # Clear existing department associations
        school.department_ID.clear()

        # Add selected departments to the school
        for department in selected_departments:
            school.department_ID.add(department)

        print(f"Assigned departments to {school.school_name}: {[dept.department_name for dept in selected_departments]}")

    print("All active schools have been updated with random departments.")

# Entry point for django-extensions
def run():
    assign_random_departments_to_schools()
