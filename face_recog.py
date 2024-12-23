import os
import csv
import cv2
import dlib
import numpy as np

# Paths to your model files (already extracted)
shape_predictor_path = "/Users/shreyyya/Desktop/face_recognition_attendance/models/shape_predictor_68_face_landmarks.dat"
face_recognition_model_path = "/Users/shreyyya/Desktop/face_recognition_attendance/models/dlib_face_recognition_resnet_model_v1.dat"
known_faces_dir = "/Users/shreyyya/Desktop/face_recognition_attendance/data /processed"  # Directory containing known face images
csv_file_path = "/Users/shreyyya/Desktop/face_recognition_attendance/models/encodings.csv"

# Load dlib models
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(shape_predictor_path)
face_recognition_model = dlib.face_recognition_model_v1(face_recognition_model_path)

# List to hold names and encodings
known_names = []
known_encodings = []

# Process each image in the known faces directory
for filename in os.listdir(known_faces_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(known_faces_dir, filename)
        image = cv2.imread(image_path)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Detect faces in the image
        faces = detector(rgb_image)
        
        # Assuming each image contains only one face
        for face in faces:
            shape = shape_predictor(rgb_image, face)
            encoding = face_recognition_model.compute_face_descriptor(rgb_image, shape)
            encoding = np.array(encoding)
            
            # Extract the name from the filename (without extension)
            name = os.path.splitext(filename)[0]
            
            known_names.append(name)
            known_encodings.append(encoding)
            break

# Save encodings and names to a CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for name, encoding in zip(known_names, known_encodings):
        writer.writerow([name] + list(encoding))

print("Encodings saved to CSV file successfully.")
