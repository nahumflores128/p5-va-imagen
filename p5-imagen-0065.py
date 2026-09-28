import cv2
# leer la imagen con cv2 = computer vision
img = cv2.imread('fornite.webp')
# determinar el tipo 
print(type(img))
# mostrar pixeles
print(img.shape)
# mostrando imagen
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()