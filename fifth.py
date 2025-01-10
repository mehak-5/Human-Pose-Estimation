import cv2
# read image as gray scale
img=cv2.imread(r'mahi.png')
#get image height,width
(h,w) =img.shape[:2]
center = (w/2, h/2)

angle90 = 90
angle180 = 180
angle270 = 270
scale = 1.0
#perform the counterclockwise rotation holding at the center
# 90 degree
M=cv2.getRotationMatrix2D(center,angle90,scale)
rotated90=cv2.warpAffine(img,M,(h,w))
#rotated180
M=cv2.getRotationMatrix2D(center,angle180,scale)
rotated180=cv2.warpAffine(img,M,(h,w))
#rotated270
M=cv2.getRotationMatrix2D(center,angle270,scale)
rotated270=cv2.warpAffine(img,M,(h,w))
cv2.imshow('original img',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imshow('image rotated by 90 degree',rotated90)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imshow('image rotated by 180 degree',rotated180)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imshow('image rotated by 270 degree',rotated270)
#cv2.waitKey(0)
#cv2.destroyAllWindows()