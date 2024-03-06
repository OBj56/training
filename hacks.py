import cv2

image = cv2.imread("liberator1.png")
image2 = cv2.imread("terrorist1.png")

cv2.imshow('image2', image) 
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()


