# Generated by Django 3.2.2 on 2021-05-13 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance_System', '0006_records_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='Name',
        ),
    ]
