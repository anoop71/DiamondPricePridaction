import cv2

def capture_and_process_photo(save_path='processed_image.png'):
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Capture a single frame
    ret, frame = cap.read()

    # Release the webcam
    cap.release()

    if not ret:
        print("Error: Could not read frame from webcam.")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        print("No faces detected.")
        return

    # Assume the first detected face is the one we want to crop
    (x, y, w, h) = faces[0]
    cropped_face = frame[y:y+h, x:x+w]

    # Convert to grayscale
    gray_image = cv2.cvtColor(cropped_face, cv2.COLOR_BGR2GRAY)

    # Put the name text on the image
    name = input("Enter the name to be put on the image: ")
    cv2.putText(gray_image, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Save the image
    cv2.imwrite(save_path, gray_image)
    print(f"Image saved at {save_path}")

# Call the function to capture and process the photo
capture_and_process_photo()
