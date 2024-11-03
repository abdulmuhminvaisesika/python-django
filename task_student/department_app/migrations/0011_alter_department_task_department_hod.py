# Generated by Django 5.1.2 on 2024-10-30 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department_app', '0010_remove_department_task_school_id'),
        ('teacher_app', '0011_remove_teachers_task_department_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department_task',
            name='department_HOD',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher_app.teachers_task'),
        ),
    ]
