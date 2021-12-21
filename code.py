import os
import shutil
import cv2
import time
import dropbox

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        result=False

    videoCaptureObject.release()    

    cv2.destroyAllWindows()

take_snapshot()    

def upload_file(image_name):
     access_token = 'aTOCzk_fQQEAAAAAAAAAAQrWvpO51eRzlt3y9W3QgtEdWZwlSHKmumydbFMu7UQ-'
     file = image_name
     file_from = file
     file_to = "/newFloder1" + (image_name)
     dbx = dropbox.Dropbox(access_token)

     with open(file_from,"rb") as f:
         dbx.files_upload(f.read(), file_to,mode = dropbox.files.WriteMode.overWrite)
         print("files uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 3):
            name = take_snapshot()
            upload_file(name)

main()
            