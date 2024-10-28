import cv2

#Loading an Image
img = cv2.imread('data\wallpaperflare.com_wallpaper (1).jpg',0)
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

img2 = img[400:, 800:]
img[:140, 800:] = img2
print(img.shape)
cv2.imshow('Solvey COnference 1928',img)
cv2.waitKey(0)
cv2.destroyAllWindows()