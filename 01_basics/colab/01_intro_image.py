import cv2

print(cv2.__version__)

image = cv2.imread(filename=r'../assets/bear.jpg')

cv2.imshow(winname='image', mat=image)
cv2.waitKey(delay=0)