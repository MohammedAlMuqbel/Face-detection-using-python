import cv2

##img=cv2.imread("Face.jpg")
##res_1=cv2.resize(img,(718,628))
##cv2.imwrite("New_Face.jpg",res_1)
##cv2.imshow("Hi",res_1)
##cv2.waitKey(0)


img=cv2.imread("Screenshot 2022-04-09 125918.png")
res_1=cv2.resize(img,(700,600))
cv2.imwrite("new screen.png",res_1)
cv2.imshow("Hi",res_1)
cv2.waitKey(0)
