# Generated by Django 5.1.2 on 2024-11-11 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_maching_app', '0001_initial'),
        ('user_profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile_table',
            name='age',
            field=models.ForeignKey(limit_choices_to={'type': 'age'}, on_delete=django.db.models.deletion.CASCADE, related_name='age_profiles', to='common_maching_app.common_matching'),
        ),
        migrations.AlterField(
            model_name='user_profile_table',
            name='caste',
            field=models.ForeignKey(limit_choices_to={'type': 'caste'}, on_delete=django.db.models.deletion.CASCADE, related_name='caste_profiles', to='common_maching_app.common_matching'),
        ),
        migrations.AlterField(
            model_name='user_profile_table',
            name='education',
            field=models.ForeignKey(limit_choices_to={'type': 'education'}, on_delete=django.db.models.deletion.CASCADE, related_name='education_profiles', to='common_maching_app.common_matching'),
        ),
        migrations.AlterField(
            model_name='user_profile_table',
            name='gender',
            field=models.ForeignKey(limit_choices_to={'type': 'gender'}, on_delete=django.db.models.deletion.CASCADE, related_name='gender_profiles', to='common_maching_app.common_matching'),
        ),
        migrations.AlterField(
            model_name='user_profile_table',
            name='height',
            field=models.ForeignKey(limit_choices_to={'type': 'height'}, on_delete=django.db.models.deletion.CASCADE, related_name='height_profiles', to='common_maching_app.common_matching'),
        ),
        migrations.AlterField(
            model_name='user_profile_table',
            name='income',
            field=models.ForeignKey(limit_choices_to={'type': 'income'}, on_delete=django.db.models.deletion.CASCADE, related_name='income_profiles', to='common_maching_app.common_matching'),
        ),
        migrations.AlterField(
            model_name='user_profile_table',
            name='language',
            field=models.ForeignKey(limit_choices_to={'type': 'language'}, on_delete=django.db.models.deletion.CASCADE, related_name='language_profiles', to='common_maching_app.common_matching'),
        ),
        migrations.AlterField(
            model_name='user_profile_table',
            name='location',
            field=models.ForeignKey(limit_choices_to={'type': 'location'}, on_delete=django.db.models.deletion.CASCADE, related_name='location_profiles', to='common_maching_app.common_matching'),
        ),
        migrations.AlterField(
            model_name='user_profile_table',
            name='marital_status',
            field=models.ForeignKey(limit_choices_to={'type': 'marital_status'}, on_delete=django.db.models.deletion.CASCADE, related_name='marital_status_profiles', to='common_maching_app.common_matching'),
        ),
        migrations.AlterField(
            model_name='user_profile_table',
            name='profession',
            field=models.ForeignKey(limit_choices_to={'type': 'profession'}, on_delete=django.db.models.deletion.CASCADE, related_name='profession_profiles', to='common_maching_app.common_matching'),
        ),
        migrations.AlterField(
            model_name='user_profile_table',
            name='religion',
            field=models.ForeignKey(limit_choices_to={'type': 'religion'}, on_delete=django.db.models.deletion.CASCADE, related_name='religion_profiles', to='common_maching_app.common_matching'),
        ),
        migrations.AlterField(
            model_name='user_profile_table',
            name='weight',
            field=models.ForeignKey(limit_choices_to={'type': 'weight'}, on_delete=django.db.models.deletion.CASCADE, related_name='weight_profiles', to='common_maching_app.common_matching'),
        ),
    ]
