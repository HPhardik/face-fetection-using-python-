import cv2
fase_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True :
    success , img = cap.read()
    face = fase_cascade.detectMultiScale(img,1.1,1)
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w ,y+h),(255,0,0),3)


    cv2.imshow('result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# press q  and window is closs 