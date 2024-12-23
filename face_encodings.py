import os
import face_recognition
import pandas as pd

def encode_faces(face_dir):
    encodings = []
    names = []

    for filename in os.listdir(face_dir):
        img_path = os.path.join(face_dir, filename)
        img = face_recognition.load_image_file(img_path)
        face_encodings = face_recognition.face_encodings(img)

        if face_encodings:
            encodings.append(face_encodings[0])
            name = filename.split('_face_')[0]  # Extract the person name
            names.append(name)
        else:
            print(f"No face encodings found for {img_path}")

    # Convert encodings to list for CSV storage
    encodings_list = [encoding.tolist() for encoding in encodings]

    # Create a DataFrame
    df = pd.DataFrame({'name': names, 'encoding': encodings_list})
    return df

# Directory containing processed images
face_dir = '/Users/shreyyya/Desktop/face_recognition_attendance/data /processed'
df = encode_faces(face_dir)

# Save to CSV
csv_path = '/Users/shreyyya/Desktop/face_recognition_attendance/models/encodings.csv'
df.to_csv(csv_path, index=False)

print(f"Encodings saved to {csv_path}")