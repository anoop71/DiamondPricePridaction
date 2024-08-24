
import cv2

def capture_photo(filename='photo.jpg'):
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    # Capture the photo
    status, photo = cap.read()

    # Check if the capture was successful
    if status:
        # Save the photo to the specified filename
        cv2.imwrite(filename, photo)
        print(f"Photo saved as {filename}")
    else:
        print("Failed to capture photo")

    # Release the resources
    cv2.destroyAllWindows()
    cap.release()

# Call the function to capture and save the photo
capture_photo()
