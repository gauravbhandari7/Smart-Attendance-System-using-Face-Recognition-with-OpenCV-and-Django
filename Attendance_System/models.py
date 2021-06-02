from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    batch = models.IntegerField(max_length=10)
    department = models.CharField(max_length=100)
    semester = models.IntegerField(max_length=5)
    image = models.ImageField(upload_to='static/images/ImagesAttendance')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk) + ' - ' + self.username


class Records(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    time = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.user) + '---' + str(self.time)


class Office_Time(models.Model):
    opening_time = models.TimeField(default="10:00:00")
    opening_time_max = models.TimeField(default="12:00:00")
    closing_time = models.TimeField(default="15:00:00")
    closing_time_max = models.TimeField(default="17:00:00")

    def __str__(self):
        return str(self.pk) + '---' + str(self.opening_time) + '---' + str(self.closing_time_max)
