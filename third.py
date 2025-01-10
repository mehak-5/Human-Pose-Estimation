import cv2 
#read image
img=cv2.imread('mahi.png',1)
#height, width, number of channels in image
dimensions=img.shape
height=img.shape[0]
width=img.shape[1]
channels=img.shape[2]
size1=img.shape
print('Image Dimension : ',dimensions)
print('Image Height : ',height)
print('Image Width: ',width)
print('Number of Channels : ',channels)
print('Image Size : ',size1)
b,g,r=cv2.split(img)
merged_img_bgr=cv2.merge((b,g,r))
merged_img_rgb=cv2.merge((r,g,b))
cv2.imshow('original image', img)
cv2.imshow('color_b_image', b)
cv2.imshow('color_g_image', g)
cv2.imshow('color_r_image', r)

cv2.imshow('merged_img_bgr',merged_img_bgr)
cv2.imshow('merged_img_rgb',merged_img_rgb)
cv2.wa