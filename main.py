#pip intall opencv-contrib-python
import cv2 as cv
# importing datetime to store multiple selfie
import datetime
capture=cv.VideoCapture(0)
face_cascade=cv.CascadeClassifier("haar_face.xml")
face_smile=cv.CascadeClassifier("ile.xml")
while True:
    ret,frame=capture.read()
    # IF YOU DONT WANT BORDERS IN IMAGE WHILE SAVING IT,CREATE A COPY OF FRAME.
    original_frame=frame.copy()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow("Camera",gray)
    face=face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=3)
    for x,y,w,h in face:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),thickness=2)
        cv.putText(frame, "Face", (x + 15, y + 15), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
        face_roi=frame[y:y+h,x:x+w]
        gray_roi=gray[y:y+h,x:x+w]
        smile=face_smile.detectMultiScale(gray_roi,1.3,5)
        for x1,y1,w1,h1 in smile:
            cv.rectangle(face_roi,(x1,y1),(x1+w1,y1+h1),(0,0,255),thickness=2)
            cv.putText(frame,"Smile",(x+100,y+100),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)            # Saving Selfie in Directory
            time_stamp=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            file_name=f"selfie-{time_stamp}.png"
            #cv.imwrite("selfie.png",original_frame)
            cv.imwrite(file_name,original_frame)
    cv.imshow("Camera_real",frame)
    if cv.waitKey(10)==ord("q"):
        break