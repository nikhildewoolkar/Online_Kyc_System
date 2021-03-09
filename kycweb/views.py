from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
from django.http.response import StreamingHttpResponse
import threading
# from .forms import FaceAdditionForm
import datetime
import os
import numpy as np
import face_recognition
import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings
from subprocess import check_output, CalledProcessError,STDOUT
# Create your views here.
# face_detection_videocam = cv2.CascadeClassifier(os.path.join(
# 			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))
def home(request):
    if request.method=='POST':
        code=0
        img=request.POST.get("filetype")
        file=str(request.FILES.get("file"))
        df=Profile(filetype=img,pic=file)
        df.save()
        print(file)
        data="media/picture/"+file
        verification1=main(data)
        data="J:/django/nikhil/projects/hackathon-kyc/kyc/face.jpg"
        verification2=facerec(data)
        if(verification1 == 1 and verification2 == 1):
            code=1
        else:
            code=0
        msg="uploaded"
        return render(request,"home.html",{"msg":msg,"code":code})
    # data='media/4.jpg'
    # facerec(data)
    return render(request,"home.html")

def index(request):
    # data='media/4.jpg'
    # facerec(data)
    return render(request,"index.html")

# def gen(camera):
#     	while True:
#             frame = camera.get_frame()
#             yield (b'--frame\r\n'
#                     b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# def video_feed(request):
# 	return StreamingHttpResponse(gen(scancam()),
# 					content_type='multipart/x-mixed-replace; boundary=frame')


# def webcam_feed(request):
# 	return StreamingHttpResponse(gen(scancam()),
# 					content_type='multipart/x-mixed-replace; boundary=frame')

# class scancam(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#     def __del__(self):
#         self.video.release()
#     def get_frame(self):
#         success, image = self.video.read()
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
#         for (x, y, w, h) in faces_detected:
#             cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
#         frame_flip = cv2.flip(image,1)
#         ret, jpeg = cv2.imencode('.jpg', frame_flip)
#         return jpeg.tobytes()
# class scancam(object):
#     def __init__(self):
#         self.video_capture = cv2.VideoCapture(0)
#     def __del__(self):
#         self.video_capture.release()
#     def get_frame(self):
#         imgAli = face_recognition.load_image_file('4.jpg')
#         imgAli_encoding = face_recognition.face_encodings(imgAli)[0]
#         known_face_encodings = [
#             imgAli_encoding,
#         ]
#         known_face_names = [
#             "Verified!"
#         ]
#         face_locations = []
#         face_encodings = []
#         face_names = []
#         process_this_frame = True
#         while True:
#             ret, frame = self.video_capture.read()
#             small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#             rgb_small_frame = small_frame[:, :, ::-1]
#             if process_this_frame:
#                 face_locations = face_recognition.face_locations(rgb_small_frame)
#                 face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
#                 face_names = []
#                 for face_encoding in face_encodings:
#                     matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#                     name = "Not Verified"
#                     face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#                     best_match_index = np.argmin(face_distances)
#                     if matches[best_match_index]:
#                         name = known_face_names[best_match_index]
#                     face_names.append(name)
#             process_this_frame = not process_this_frame
#             for (top, right, bottom, left), name in zip(face_locations, face_names):
#                 top *= 4
#                 right *= 4
#                 bottom *= 4
#                 left *= 4
#                 cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#                 cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#                 font = cv2.FONT_HERSHEY_DUPLEX
#                 cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#             cv2.imshow('Video', frame)
#             ret,jpeg = cv2.imencode('.jpg', frame)
#             return jpeg.tobytes()            

def facerec(data):
    video_capture = cv2.VideoCapture(0)
    imgAli = face_recognition.load_image_file(data)
    imgAli_encoding = face_recognition.face_encodings(imgAli)[0]
    known_face_encodings = [
        imgAli_encoding,
    ]
    known_face_names = [
        "verified"
    ]
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Not Verified"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                face_names.append(name)
        process_this_frame = not process_this_frame
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()


import pytesseract
from PIL import Image
import datetime
import cv2
import sys
import os
import os.path
import re
import numpy as np
from pyzbar.pyzbar import decode
# Function to extract the text from image as string
def extract_text(image_file):
    # img=Image.open(self.image_file)
    img = cv2.imread(image_file)
    print("image reading successful")
    # resize the image
    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    print("image resizing successful")
    print("dimension: ",img.shape)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # convert the image to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # C:/Program Files/Tesseract-OCR/tessdata
    # the following command uses the tesseract directory path to get the trained data in the config option
    text = pytesseract.image_to_string(img, config='--tessdata-dir "J:/django/nikhil/projects/hackathon-kyc/kyc/tessdata"')
    return text

def is_aadhar_card(text):
    res = text.split()
    gIndex = 0
    gender = ""
    # print("all data: ",res)
    if 'Government of India' in text:
        print("Aadhar card is valid and the details are below:")
        for l in res:
            if 'DOB' in l:
                index = res.index(l)
            if l=="MALE" or l=="FEMALE":
                gIndex = res.index(l)
                gender = res[gIndex]
        name = ''
        if res[index - 4].isalpha():
            name = res[index - 4] + " " + res[index - 3] + " " + res[index - 2]
    else:
        name = res[0] + " " + res[1]
    if len(name) > 1:
        print("Name:  " + name)
    else:
        print("Name not read")
    # dob_index = res.index()
    date = res[index+1]
    print("DOB: ",date)
    aadhar_number = ''
    for word in res:
        if len(word) == 4 and word.isdigit():
            aadhar_number = aadhar_number + word
            # print("Aadhar Building: ", aadhar_number)
            if len(aadhar_number)==12:
                break
    print("Aadhar number is: " + aadhar_number)
    print("Gender: ",gender)
    qrImg = cv2.imread('QRFullDetect.jpg')
    df, d = readBarcodeQRcode(qrImg)
    # print("Data: ",df)
    # print("Label: ",d)
    if aadhar_number == df[d.index("uid")] and name == df[d.index("name")]:
        print("Data match")
        return 1
    else:
        print("Data mismatch.")
        return 0

def extractFace(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        faces = img[y:y + h, x:x + w]
        cv2.imshow("face", faces)
        cv2.imwrite('face.jpg', faces)
    cv2.imwrite('detcted.jpg', img)
    cv2.imshow('img', img)
    cv2.waitKey()
    # return faces

def readBarcodeQRcode(img):
    # img = cv2.imread('test1_back.png')
    img = cv2.imread('QRFullDetect.jpg')
    for barcode in decode(img):
        data = barcode.data
        myData = barcode.data.decode('utf-8')
        # print(myData)
    # myData = myData.split()
    print("List: ", myData)
    d = ["uid", "name", "gender", "yob", "gname", "co", "house", "lm", "loc", "vtc", "po", "dist", "subdist", "state",
         "pc"]
    def stringToList(string):
        l = []
        flag = 0
        for c in string:
            if flag:
                if c != '"':
                    str += c
                else:
                    l.append(str)
                    flag = 0
            elif c == '"':
                str = ''
                flag = 1
        return l
    df = stringToList(myData)
    del df[0:2]
    print(df)
    print(df[d.index("name")])
    return df, d

def main(data):
    # image_file_name = "test2.png"
    image_file_name = data
    # Check for right infilename extension.
    print("file name: ",image_file_name)
    file_ext = os.path.splitext(image_file_name)[1]
    print("File extension: ",file_ext)
    if file_ext.upper() not in ('.JPG', '.PNG'):
        print("Input filename extension should be .JPG or .PNG")
        sys.exit(1)
    text = extract_text(image_file_name)
    # text = te.extract_text()
    g=is_aadhar_card(text)
    extractFace(image_file_name)
    return g












# from django.shortcuts import render
# from .forms import FaceAdditionForm
# import cv2
# import numpy as np
# from django.http import StreamingHttpResponse

# def capture_video_from_cam():
#     cap = cv2.VideoCapture(0)
#     currentFrame = 0
#     while True:

#         ret, frame = cap.read()

#         # Handles the mirroring of the current frame
#         frame = cv2.flip(frame,1)
#         currentFrame += 1

# def addfaces(request):
#     add_faces_form = FaceAdditionForm()
#     if add_faces_form.is_valid():
#         add_faces_form.save()
#     return render(request, 'home.html', {'add_faces': add_faces_form})


# def show_video_on_page(request):
#     resp = StreamingHttpResponse(capture_video_from_cam())
#     return render(request, 'home.html', {'video': resp})
# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         image = self.frame
#         ret, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()

#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()


# cam = VideoCamera()


# def gen(camera):
#     while True:
#         frame = cam.get_frame()
#         yield(b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# @gzip.gzip_page
# def livefe(request):
#     try:
#         return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:  # This is bad! replace it with proper handling
#         pass