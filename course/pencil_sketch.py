import cv2


image_path = './db/cat.jpg'  
original_image = cv2.imread(image_path)
# adapter la taille
original_image = cv2.resize(original_image, (500, 500))


gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

inverted_image = cv2.bitwise_not(gray_image)


blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)


inverted_blurred_image = cv2.bitwise_not(blurred_image)


pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

cv2.imshow('Original Image', original_image)
cv2.imshow('Pencil Sketch', pencil_sketch_image)


cv2.imwrite('output_pencil_sketch.jpg', pencil_sketch_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
