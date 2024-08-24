from cvzone.PoseModule import PoseDetector
import cv2
import pygame

# Initialize the webcam (change the index as needed)
cap = cv2.VideoCapture(0)

# Initialize the PoseDetector class with the given parameters
detector = PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)

# Initialize pygame mixer for playing the audio
pygame.mixer.init()
audio_path = ''  # Replace with the correct path to your audio file
pygame.mixer.music.load(audio_path)

# Function to play the audio if not already playing
def play_audio():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

# Loop to continuously get frames from the webcam
while True:
    # Capture each frame from the webcam
    success, img = cap.read()

    if not success:
        print("Failed to capture image")
        break

    # Find the human pose in the frame
    img = detector.findPose(img)

    # Find the landmarks, bounding box, and center of the body in the frame
    lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=True)

    # Check if any body landmarks are detected
    if lmList:
        # Example: Check if hand is holding a rolled paper (just a conceptual example)
        # Adjust these indices based on your specific gesture detection logic
        left_hand_thumb_tip = 4
        right_hand_index_tip = 8

        # Condition to detect rolled paper (example)
        if (lmList[left_hand_thumb_tip][1] < lmList[right_hand_index_tip][1]):  # Assuming left thumb is lower than right index finger
            print("Rolled paper gesture detected")
            play_audio()

        # Draw a circle at the center of the bounding box
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

        # Calculate the distance between landmarks 11 and 15 and draw it on the image
        length, img, info = detector.findDistance(lmList[11][0:2],
                                                  lmList[15][0:2],
                                                  img=img,
                                                  color=(255, 0, 0),
                                                  scale=10)

        # Calculate the angle between landmarks 11, 13, and 15 and draw it on the image
        angle, img = detector.findAngle(lmList[11][0:2],
                                        lmList[13][0:2],
                                        lmList[15][0:2],
                                        img=img,
                                        color=(0, 0, 255),
                                        scale=10)

        # Check if the angle is close to 50 degrees with an offset of 10
        isCloseAngle50 = detector.angleCheck(myAngle=angle,
                                             targetAngle=50,
                                             offset=10)

        # Print the result of the angle check
        print(isCloseAngle50)

    # Display the frame in a window
    cv2.imshow("Image", img)

    # Wait for 1 millisecond between each frame
    if cv2.waitKey(1) == 13:  # Press Enter to exit
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()