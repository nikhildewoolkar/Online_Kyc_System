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

def main():
    image_file_name = "test2.png"
    # Check for right infilename extension.
    print("file name: ",image_file_name)
    file_ext = os.path.splitext(image_file_name)[1]
    print("File extension: ",file_ext)
    if file_ext.upper() not in ('.JPG', '.PNG'):
        print("Input filename extension should be .JPG or .PNG")
        sys.exit(1)
    text = extract_text(image_file_name)
    # text = te.extract_text()
    is_aadhar_card(text)
    extractFace(image_file_name)
main()