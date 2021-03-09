# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pytesseract
from PIL import Image
import datetime
import cv2
import sys
import os
import os.path
import re
import numpy as np


# class to extract text from an image where the image file is passed as an argument
class Text_Extractor():
    # Constructor
    def __init__(self, image_file):
        self.image_file = image_file
        if self is None:
            return 0

    # Function to extract the text from image as string
    def extract_text(self):
        # img=Image.open(self.image_file)
        img = cv2.imread(self.image_file)
        # resize the image
        img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        # convert the image to gray
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # the following command uses the tesseract directory path to get the trained data in the config option
        text = pytesseract.image_to_string(img, config='--tessdata-dir "/usr/local/Cellar/tesseract/4.0.0_1/share/tessdata"')
        return text

# class to validate if  an image is a adhar card where the text is passed as an argument
class Aadhar_Card_Validator():
    # Constructor
    def __init__(self, text):
        self.text = text

    # Function to validate if an image contains text showing its an aadhar card
    def is_aadhar_card(self):
        res = self.text.split()
        dates = {}
        if 'GOVERNMENT OF INDIA' in self.text:
            print("Aadhar card is valid and the details are below:")
            index = res.index('INDIA')
            name = ''
            if res[index + 3].isalpha():
                name = res[index + 3] + " " + res[index + 4] + " " + res[index + 5]
            else:
                name = res[index + 4] + " " + res[index + 5] + " " + res[index + 6]
        else:
            name = res[0] + " " + res[1]
        if len(name) > 1:
            print("Name:  " + name)
        else:
            print("Name not read")
        p = re.compile('d+/d+/d+')
        if (p.findall(self.text)):
            dates = p.findall(self.text)

        if len(dates) > 0 and len(dates[0]) > 1:
            print("Date of birth:" + str(dates[0]))
        aadhar_number = ''
        for word in res:
            if 'yob' in word.lower():
                yob = re.findall('d+', word)
                if yob:
                    print('Year of Birth: ' + yob[0])
            if len(word) == 4 and word.isdigit():
                aadhar_number = aadhar_number + word + ' '
        if len(aadhar_number) >= 14:
            print("Aadhar number is :" + aadhar_number)
        else:
            print("Aadhar number not read")
            print("Try again or try  another file")

def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
        sys.exit(1)
    image_file_name = sys.argv[1]
    # Check for right infilename extension.
    file_ext = os.path.splitext(image_file_name)[1]
    if file_ext.upper() not in ('.JPG', '.PNG'):
        print("Input filename extension should be .JPG or .PNG")
        sys.exit(1)
    te = Text_Extractor(image_file_name)
    text = te.extract_text()
    acv = Aadhar_Card_Validator(text)
    acv.is_aadhar_card()

main()