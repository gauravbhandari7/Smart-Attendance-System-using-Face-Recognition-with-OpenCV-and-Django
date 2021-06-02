# Generated by Django 3.2.2 on 2021-06-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance_System', '0015_auto_20210601_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office_time',
            name='closing_time',
            field=models.TimeField(default='15:00:00'),
        ),
        migrations.AlterField(
            model_name='office_time',
            name='closing_time_max',
            field=models.TimeField(default='17:00:00'),
        ),
        migrations.AlterField(
            model_name='office_time',
            name='opening_time_max',
            field=models.TimeField(default='12:00:00'),
        ),
    ]
