import csv
import cv2
import dlib
import numpy as np
import face_recognition
from imutils import face_utils

# Paths to your model files (replace with your actual paths)
shape_predictor_path = '/Users/shreyyya/Desktop/face_recognition_attendance/models/shape_predictor_68_face_landmarks.dat'
face_recognition_model_path = '/Users/shreyyya/Desktop/face_recognition_attendance/models/dlib_face_recognition_resnet_model_v1.dat'
csv_file_path = '/Users/shreyyya/Desktop/face_recognition_attendance/models/encodings.csv'

# Load dlib models
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(shape_predictor_path)
face_rec_model = dlib.face_recognition_model_v1(face_recognition_model_path)

# Load known face encodings and names from CSV
known_face_encodings = []
known_face_names = []

with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        known_face_names.append(row[0])
        known_face_encodings.append(np.array(row[1:], dtype=float))

print(f"Loaded {len(known_face_encodings)} known face encodings.")

# Initialize webcam
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:
        print("Error: Could not read frame from webcam.")
        break

    # Convert the BGR frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    faces = detector(rgb_frame, 1)

    for face in faces:
        # Determine the facial landmarks for the face region
        shape = shape_predictor(rgb_frame, face)
        
        # Compute the 128D vector that describes the face
        face_encoding = np.array(face_rec_model.compute_face_descriptor(rgb_frame, shape))

        # Compare the encoding with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Draw a rectangle around the face
        (x, y, w, h) = face_utils.rect_to_bb(face)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (x, y + h + 15), (x + w, y + h + 35), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (x + 6, y + h + 30), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
