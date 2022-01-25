import cv2
import cvzone
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


button = input("for native enter 'n'\n , "
               "for sunglass enter 's'\n , "
               "for star enter 't'\n,"
               "for pirate enter 'p',"
               "for beard enter 'c'\n,"
               "for cool enter 'c'\n:=\n")
if button == 'n':
    img = cv2.imread('native.png',cv2.IMREAD_UNCHANGED)
elif button == 's':
    img = cv2.imread('sunglass.png',cv2.IMREAD_UNCHANGED)
elif button == 't':
    img = cv2.imread('star.png',cv2.IMREAD_UNCHANGED)
elif button == 'b':
    img = cv2.imread('beard.png',cv2.IMREAD_UNCHANGED)
elif button == 'c':
    img = cv2.imread('cool.png',cv2.IMREAD_UNCHANGED)
else:
    if button == 'p':
        img = cv2.imread('pirate.png',cv2.IMREAD_UNCHANGED)





while True:



    red,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in face:
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        overlay_resize = cv2.resize(img,(int(w*1.5),int(h*1.5)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x-45,y-75])

    cv2.imshow('snap',frame)

    if cv2.waitKey(10) == ord('q'):
        break
