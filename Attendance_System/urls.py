from django.conf.urls import url
from . import views

urlpatterns = [
    # /Attendance_System/
    url(r'^$', views.index, name='index'),
    # /Attendance_System/validate
    url(r'home/', views.home, name='home'),
    url(r'webcam/', views.webcam, name='webcam'),
    url(r'check_attendance/', views.check_attendance, name='check_attendance'),
    url(r'logout_user/', views.logout_user, name='logout_user'),
    url(r'attendance_check/', views.attendance_check, name='attendance_check'),
]
