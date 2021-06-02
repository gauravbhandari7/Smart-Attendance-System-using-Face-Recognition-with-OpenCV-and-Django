# Generated by Django 3.2.2 on 2021-06-01 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance_System', '0013_office_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office_time',
            name='closing_time',
        ),
        migrations.RemoveField(
            model_name='office_time',
            name='closing_time_max',
        ),
        migrations.RemoveField(
            model_name='office_time',
            name='opening_time_max',
        ),
        migrations.AlterField(
            model_name='office_time',
            name='opening_time',
            field=models.TimeField(default='12:00:00'),
        ),
    ]