from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    batch = models.IntegerField(max_length=10)
    department = models.CharField(max_length=100)
    semester = models.IntegerField(max_length=5)
    image = models.ImageField(upload_to='static/images/ImagesAttendance')
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk) + ' - ' + self.name + ' - ' + self.department


class Records(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    time = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.user) + '---' + str(self.time)
