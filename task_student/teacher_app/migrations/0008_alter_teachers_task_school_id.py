# Generated by Django 5.1.2 on 2024-10-28 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0003_rename_active_on_school_task_is_active'),
        ('teacher_app', '0007_rename_active_on_teachers_task_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers_task',
            name='school_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='teachers', to='school_app.school_task'),
        ),
    ]
