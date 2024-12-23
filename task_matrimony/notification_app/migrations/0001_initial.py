# Generated by Django 5.1.2 on 2024-11-20 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile_app', '0003_alter_user_profile_table_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification_Table',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('notification_type', models.CharField(max_length=255)),
                ('notification_message', models.TextField()),
                ('notification_date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile_app.user_profile_table')),
            ],
        ),
    ]
