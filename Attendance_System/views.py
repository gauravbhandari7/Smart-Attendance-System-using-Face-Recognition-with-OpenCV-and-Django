import os
import cv2
import numpy as np
import face_recognition
from datetime import datetime,  date
import pyttsx3
from Face_Recognition.settings import BASE_DIR
from django.shortcuts import render
from Attendance_System.models import *
from django.contrib.auth import authenticate, logout, login

date_today = date.today()
today_date = date_today.strftime("%Y-%m-%d")


def index(request):
    if request.user.is_authenticated:
        return render(request, 'Attendance_System/admin_home.html')
    else:
        return render(request, 'Attendance_System/index.html')


def logout_user(request):
    logout(request)
    return render(request, 'Attendance_System/index.html')


def attendance_check(request):
    user = UserInfo.objects.all()
    context = {'today_date': today_date, 'user': user}
    if request.method == 'POST':
        selected_user = request.POST['selected_user']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        name = "Name"
        time = "Time"
        result = Records.objects.filter(time__range=(start_date, end_date))
        result1 = Records.objects.filter(user__name=selected_user, time__range=(start_date, end_date))
        if selected_user == "all" and result:
            context = {'today_date': today_date, 'result': result, 'user': user, 'name': name, 'time': time}
            return render(request, 'Attendance_System/attendance_check.html', context)
        elif result1:
            context = {'today_date': today_date, 'result': result1, 'user': user, 'name': name, 'time': time}
            return render(request, 'Attendance_System/attendance_check.html', context)
        else:
            error = "No records found"
            context = {'today_date': today_date, 'error': error, 'user': user, 'name': name, 'time': time}
            return render(request, 'Attendance_System/attendance_check.html', context)

    else:
        return render(request, 'Attendance_System/attendance_check.html', context)


def profile(request):
    user = UserInfo.objects.get(username=request.session['username'], password=request.session['password'])
    return render(request, 'Attendance_System/profile.html', {'user': user})


def home(request):
    if request.user.is_authenticated:
        return render(request, 'Attendance_System/admin_home.html')

    elif request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['pass']
        request.session['username'] = uname
        request.session['password'] = password
        user_existence = UserInfo.objects.filter(username=uname, password=password)
        user_admin = authenticate(request, username=uname, password=password)
        if user_existence:
            user = UserInfo.objects.get(username=uname, password=password)
            return render(request, 'Attendance_System/user_home.html', {'user': user})
        elif user_admin is not None:
            login(request, user_admin)
            return render(request, 'Attendance_System/admin_home.html')
        else:
            error = "Invalid username or password"
            return render(request, 'Attendance_System/index.html', {'error': error})

    else:
        user = UserInfo.objects.get(username=request.session['username'], password=request.session['password'])
        return render(request, 'Attendance_System/user_home.html', {'user': user})


def check_attendance(request):
    user = UserInfo.objects.get(username=request.session['username'], password=request.session['password'])
    if request.method == 'POST':
        time ="Time"
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        name = request.POST['name']
        result = Records.objects.filter(user__name=name, time__range=(start_date, end_date))
        if result:
            return render(request, 'Attendance_System/check.html', {'today_date': today_date, 'user': user, 'result': result, 'time': time})
        else:
            error = "No records found"
            return render(request, 'Attendance_System/check.html', {'today_date': today_date, 'user': user, 'error': error, 'time': time})
    else:
        return render(request, 'Attendance_System/check.html', {'today_date': today_date, 'user': user})


converter = pyttsx3.init()
path = os.path.join(BASE_DIR, 'static/images/ImagesAttendance')
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    cl = cl.replace("_", " ")
    classNames.append(os.path.splitext(cl)[0])


def findEncodings(images):
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


def markAttendance(name):
    today = date.today()
    now = datetime.now()
    office_time = Office_Time.objects.get(pk=1)
    
    opening_time = datetime(today.year, today.month, today.day, office_time.opening_time.hour
                                               , office_time.opening_time.minute, office_time.opening_time.second)
    
    opening_time_max = datetime(today.year, today.month, today.day,  office_time.opening_time_max.hour
                                  , office_time.opening_time_max.minute, office_time.opening_time_max.second)

    closing_time = datetime(today.year, today.month, today.day, office_time.closing_time.hour,
                            office_time.closing_time.minute, office_time.closing_time.second)
    
    closing_time_max = datetime(today.year, today.month, today.day, office_time.closing_time_max.hour,
                                  office_time.closing_time_max.minute, office_time.closing_time_max.second)


    if now < opening_time_max and now > opening_time:

        result1 = Records.objects.filter(user__name=name, time__range=(opening_time, opening_time_max))

        if not result1:
            user_object = UserInfo.objects.get(name=name)
            record = Records(user=user_object, time=now)
            record.save()
            converter.say("Hello" + name + "Your attendance is recorded")
            converter.runAndWait()

        else:
            converter.say("Hello" + name + "Your morning attendance is already recorded")
            converter.runAndWait()

    elif now > closing_time and now < closing_time_max:

        result1 = Records.objects.filter(user__name=name,time__range=(closing_time, closing_time_max))

        if not result1:
            user_object = UserInfo.objects.get(name=name)
            record = Records(user=user_object, time=now)
            record.save()
            converter.say("Hello" + name + "Your attendance is recorded")
            converter.runAndWait()

        else:
            converter.say("Hello" + name + "Your evening attendance is already recorded")
            converter.runAndWait()

    else:
        converter.say("Hello" + name + "This is not the proper time")
        converter.runAndWait()

def webcam(request):
    encodeListKnown = findEncodings(images)
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if faceDis[matchIndex] < 0.50:
                name = classNames[matchIndex]
                markAttendance(name)

            else:
                name = 'Unknown'
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            cv2.imshow('Webcam', img)
            cv2.waitKey(1)
