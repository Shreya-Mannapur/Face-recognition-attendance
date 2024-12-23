import os
import csv
import cv2
import dlib
import numpy as np
from datetime import datetime

# Paths to your model files
shape_predictor_path = "/Users/shreyyya/Desktop/face_recognition_attendance/models/shape_predictor_68_face_landmarks.dat"
face_recognition_model_path = "/Users/shreyyya/Desktop/face_recognition_attendance/models/dlib_face_recognition_resnet_model_v1.dat"
csv_file_path = "/Users/shreyyya/Desktop/face_recognition_attendance/models/encodings.csv"
attendance_file_path = "/Users/shreyyya/Desktop/face_recognition_attendance/models/attendance.csv"

# Load dlib models
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(shape_predictor_path)
face_recognition_model = dlib.face_recognition_model_v1(face_recognition_model_path)

# Load known face encodings and names from CSV
known_names = []
known_encodings = []

with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        known_names.append(row[0])
        known_encodings.append(np.array(row[1:], dtype=float))

print(f"Loaded {len(known_encodings)} known face encodings.")

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Dictionary to track attendance
attendance = {}

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces in the frame
    faces = detector(rgb_frame)

    for face in faces:
        shape = shape_predictor(rgb_frame, face)
        encoding = face_recognition_model.compute_face_descriptor(rgb_frame, shape)
        encoding = np.array(encoding)

        # Compare with known encodings
        matches = []
        for known_encoding in known_encodings:
            distance = np.linalg.norm(known_encoding - encoding)
            matches.append(distance)

        # Find the best match if matches are not empty
        if matches:
            min_distance_index = np.argmin(matches)
            min_distance = matches[min_distance_index]

            # If the minimum distance is below a threshold, we consider it a match
            if min_distance < 0.6:
                name = known_names[min_distance_index]
            else:
                name = "Unknown"
        else:
            name = "Unknown"

        # Record attendance if the person is recognized
        if name != "Unknown":
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            attendance[name] = current_time

        # Draw a rectangle around the face and label the name
        (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Save attendance to CSV
with open(attendance_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Time"])
    for name, time in attendance.items():
        writer.writerow([name, time])

# Release the capture and close the window
video_capture.release()
cv2.destroyAllWindows()

print("Attendance saved successfully.")