# Generated by Django 5.1.2 on 2024-11-22 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcription_app', '0002_subcriptionsforuser'),
        ('user_app', '0006_alter_customuser_subcription_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='subcription_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subcription_app.subcriptionsforuser'),
        ),
    ]