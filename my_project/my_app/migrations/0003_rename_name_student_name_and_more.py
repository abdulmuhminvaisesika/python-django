# Generated by Django 5.1.2 on 2024-10-17 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_student_roll_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='roll_no',
            new_name='Roll_no',
        ),
    ]