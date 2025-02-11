import cv2
import mediapipe as mp

# Initialize PoseNet and Hand Detection
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

pose = mp_pose.Pose(static_image_mode=False, model_complexity=2, 
                     min_detection_confidence=0.8, min_tracking_confidence=0.8)

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

# Open webcam with higher resolution
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to capture frame")
        break

    # Convert to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process pose detection
    pose_result = pose.process(rgb_frame)
    if pose_result.pose_landmarks:
        mp_drawing.draw_landmarks(frame, pose_result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Process hand detection
    hand_result = hands.process(rgb_frame)
    if hand_result.multi_hand_landmarks:
        for hand_landmarks in hand_result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Example: detect whether the hand is holding an object (simplified example)
            print("Hand detected!")

    # Show output
    cv2.imshow("Pose and Hand Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
