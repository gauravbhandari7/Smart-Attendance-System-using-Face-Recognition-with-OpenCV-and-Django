# Generated by Django 3.2.2 on 2021-05-13 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance_System', '0005_remove_records_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='User',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Attendance_System.userinfo'),
            preserve_default=False,
        ),
    ]
