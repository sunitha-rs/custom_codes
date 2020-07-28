
# case1:
'''
import cv2

img = cv2.imread('crystall_ball.jfif',-1)
print(img)

cv2.imshow('image',img) # displaying the image from the file
cv2.waitKey(0) 
cv2.destroyAllWindows() # killing all windows

cv2.imwrite('crystall_ball_copy.png',img)'''



# case2: 

import cv2

img = cv2.imread('crystall_ball.jfif',-1)
print(img)

cv2.imshow('image',img) 
k=cv2.waitKey(0) & 0xFF

if k == 27:  # ascii of escape key is 27
	cv2.destroyAllWindows() 
elif k == ord('s'):	
	cv2.imwrite('crystall_ball_copy.png',img)
	cv2.destroyAllWindows() 