# Generated by Django 5.1.2 on 2024-11-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferance_app', '0006_alter_preference_caste_alter_preference_education_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='marital_status',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
