import numpy as np
import cv2

# cap = cv2.VideoCapture('data\AMAZING.mp4')
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # width = int(cap.get(3))
    # height = int(cap.get(4))

    # image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # image[height//2:, :width//2] = smaller_frame
    # image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', smaller_frame)

    if cv2.waitKey(100) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

## outing 20 images in the window

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Create an empty black image to hold the smaller frames in a grid
    image = np.zeros(frame.shape, np.uint8)

    # Resize each frame to 1/5th width and 1/4th height to fit a 5x4 grid
    smaller_frame = cv2.resize(frame, (width // 5, height // 4))

    # Place the smaller frames in a 4x5 grid
    for i in range(4):
        for j in range(5):
            if (i + j) % 2 == 0:  # Alternate rotations
                rotated_frame = cv2.rotate(smaller_frame, cv2.ROTATE_180)
            else:
                rotated_frame = smaller_frame

            # Calculate the starting x and y positions
            x_start = j * smaller_frame.shape[1]
            y_start = i * smaller_frame.shape[0]

            # Place the frame on the grid
            image[y_start:y_start + smaller_frame.shape[0], x_start:x_start + smaller_frame.shape[1]] = rotated_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')


print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')
