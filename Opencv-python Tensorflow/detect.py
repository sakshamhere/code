import classify
import cv2
import csv
import time


face_cascade = cv2.CascadeClassifier('C:\\Users\\user\\Documents\\python\\Face-recognition\\final\\Test\\haarcascade_frontalface_default.xml')
size =4

webcam = cv2.VideoCapture(0)




while True:
    flag,img = webcam.read()
    img = cv2.flip(img,1,0) #flip to act as mirror

    if flag:
       # resize = cv2.resize(img,(int(img.shape[0]/size),int(img.shape[1]/size))) #resizing to enhance detection

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #cv2 supports grayscale 

        faces = face_cascade.detectMultiScale(gray,1.3,1) #getting coordinates

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
        
            sub_face = img[y:y+h,x:x+h] #taking only face
    
            cv2.imwrite('test.jpg',sub_face) #saving current image for testing

            text = classify.main('test.jpg') #get the classification result from classify.py
            #text = text.title()
            font = cv2.FONT_HERSHEY_PLAIN
             

            with open('data.csv') as f:
                data = csv.reader(f)
                next(data)
                for details in data:
                    if details[0] == text.title():
                        cv2.putText(img,'Name: ' + details[0],(x+w+20,y), font, 1, (0,0,255), 2)
                        cv2.putText(img,'Surname: ' + details[1],(x+w+20,y+40), font, 1, (0,0,255), 2)
                        cv2.putText(img,'Age: ' + details[2],(x+w+20,y+100), font, 1, (0,0,255), 2)
                        cv2.putText(img,'Roll-no: ' + details[3],(x+w+20,y+h), font, 1, (0,0,255), 2)
                        
                        print(text.title())
                    else:
                        pass
                        # time.sleep(3)
                        # cv2.putText(img,'UNknown',(x+w+20,y+50), font, 1, (0,0,255), 2)
        
        cv2.imshow('img',img)
        key = cv2.waitKey(10)
        #if esc pressed break the loop
        if key == 27:
            break


