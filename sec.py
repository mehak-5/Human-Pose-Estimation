import cv2
img=cv2.imread(r'mahi.png',0)
print(img)
status = cv2.imwrite('mahi.png',img)
print("image written to file-system: ",status)