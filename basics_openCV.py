import cv2

#Loading an Image
img = cv2.imread('data\wallpaperflare.com_wallpaper (1).jpg',1)
#Resizing the image
# img = cv2.resize(img,(1000,500))
#Scale the Axes
img = cv2.resize(img,(0,0),fx=0.5,fy = 0.5)
#rotating image
# img2 = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
#saving the image
cv2.imwrite('data\half_size.jpg',img)


cv2.imshow('Solvey COnference 1928',img)
# cv2.waitKey(0)
# cv2.imshow('Solvey COnference 1928',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
