import cv2
import dlib
import numpy as np

# Load the pre-trained face detection model from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the pre-trained facial landmark detection model from dlib
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initialize the video capture using the default camera (0)
cap = cv2.VideoCapture(0)

# Create a window to display the video feed
cv2.namedWindow("Headshot Tracking", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Calculate the center of the detected face
        face_center = (x + w // 2, y + h // 2)

        # Use dlib to detect facial landmarks
        rect = dlib.rectangle(x, y, x + w, y + h)
        shape = predictor(gray, rect)

        # Get the 28th landmark (between the eyebrows) and move it slightly upward
        target_x, target_y = shape.part(27).x, shape.part(27).y - 30  # Adjust the -30 to move it up

        # Display the coordinates at the top left corner
        cv2.putText(frame, f"X: {target_x}, Y: {target_y}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

        # Display "Target locked" on the top right corner
        cv2.putText(frame, "Target locked", (frame.shape[1] - 230, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Calculate the center of the circle based on the red dot's position
        circle_center = (target_x, target_y)

        # Set the radius of the circle
        circle_radius = 50

        # Draw a red circle with only the outer line
        cv2.circle(frame, circle_center, circle_radius, (0, 0, 255), 2, lineType=cv2.LINE_AA)

        # Calculate the endpoints for the horizontal line
        line_x1, line_y1 = 0, target_y
        line_x2, line_y2 = frame.shape[1], target_y

        # Calculate the endpoints for the vertical line
        line_x3, line_y3 = target_x, 0
        line_x4, line_y4 = target_x, frame.shape[0]

        # Draw red horizontal and vertical lines
        cv2.line(frame, (line_x1, line_y1), (line_x2, line_y2), (0, 0, 0), 2, lineType=cv2.LINE_AA)
        cv2.line(frame, (line_x3, line_y3), (line_x4, line_y4), (0, 0, 0), 2, lineType=cv2.LINE_AA)

        # Draw a red dot on the target's forehead
        cv2.circle(frame, (target_x, target_y), 15, (0, 0, 255), -1)

    cv2.imshow("Headshot Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the video capture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
