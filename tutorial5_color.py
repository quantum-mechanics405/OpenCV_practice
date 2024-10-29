import cv2
import numpy as np

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Define the lower and upper boundaries for the blue color in HSV
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply the mask to get only the blue parts of the image
    blue_only = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame and the filtered blue image
    cv2.imshow('Original', frame)
    cv2.imshow('Blue Only', blue_only)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('a'):
        break

# Release the capture and close windows
cap.release() 
cv2.destroyAllWindows()  
