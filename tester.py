import cv2
import os

def detect_and_save_faces():
    # Create directory for saving images if it doesn't exist
    output_dir = "data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Initialize face detector
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    if face_classifier.empty():
        print("Error: Haar cascade file not found.")
        return

    def face_cropped(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
        if len(faces) == 0:
            print("No faces detected.")
        for (x, y, w, h) in faces:
            return img[y:y+h, x:x+w]
        return None

    # Capture images for dataset
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    img_id = 0
    while True:
        ret, my_frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        face = face_cropped(my_frame)
        if face is not None:
            img_id += 1
            face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            file_name_path = os.path.join(output_dir, f"user_face_{img_id}.jpg")
            cv2.imwrite(file_name_path, face_gray)
            print(f"Image saved: {file_name_path}")  # Debug: Confirm image saving
            cv2.putText(face_gray, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Cropped Face", face_gray)

        # Display the video feed
        cv2.imshow("Video Feed", my_frame)

        # Break the loop if 'Enter' key is pressed or 100 images are saved
        if cv2.waitKey(1) == 13 or img_id >= 100:
            break

    cap.release()
    cv2.destroyAllWindows()

    print("Face detection and image saving completed.")

# Call the function to test
detect_and_save_faces()
