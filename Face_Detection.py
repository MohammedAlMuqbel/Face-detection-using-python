import cv2

face_detect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("KoKy_2.jpg") ## Here You put the picture name and its extention

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_detect.detectMultiScale(gray,
scaleFactor=1.05,
minNeighbors = 5 )

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

print(type(faces))
print(faces)


cv2.imshow("grey",img)
cv2.waitKey(0)
