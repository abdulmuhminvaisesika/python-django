# Generated by Django 5.1.2 on 2024-10-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers_task',
            name='employee_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]