# Generated by Django 3.2.2 on 2021-05-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance_System', '0003_userinfo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='Name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='records',
            name='Time',
            field=models.DateTimeField(null=True),
        ),
    ]
