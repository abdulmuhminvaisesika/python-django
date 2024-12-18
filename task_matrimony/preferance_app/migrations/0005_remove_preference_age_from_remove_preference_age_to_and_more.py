# Generated by Django 5.1.2 on 2024-11-14 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferance_app', '0004_rename_age_preference_age_from_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='age_from',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='age_to',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='height_from',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='height_to',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='income_from',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='income_to',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='weight_from',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='weight_to',
        ),
        migrations.AddField(
            model_name='preference',
            name='age_range',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='preference',
            name='height_range',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='preference',
            name='income_range',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='preference',
            name='weight_range',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
