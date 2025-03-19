import cv2

# Load the video file
cap = cv2.VideoCapture("data\AMAZING.mp4")

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    # Get frame rate (FPS)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    
    # Get total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Calculate video duration in seconds
    duration = total_frames / fps if fps else 0
    
    # Print the results
    print(f"Frame Rate (FPS): {fps}")
    print(f"Total Frames: {total_frames}")
    print(f"Duration (seconds): {duration}")
    print(f"Duration (minutes:seconds): {int(duration // 60)}:{int(duration % 60)}")

# Release the capture when done
cap.release()
