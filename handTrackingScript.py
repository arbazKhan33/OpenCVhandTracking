import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Custom drawing specifications
drawing_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=2, color=(255, 0, 0))  # red color for nodes
vein_spec = mp_drawing.DrawingSpec(thickness=1, color=(0, 255, 0))  # green color for lines


def draw_vein_like_structure(image, landmarks):
    # This function draws more intricate lines to mimic veins or a neural network
    for landmark in landmarks.landmark:
        x = int(landmark.x * image.shape[1])
        y = int(landmark.y * image.shape[0])
        for nearby_landmark in landmarks.landmark:
            nx = int(nearby_landmark.x * image.shape[1])
            ny = int(nearby_landmark.y * image.shape[0])
            cv2.line(image, (x, y), (nx, ny), vein_spec.color, vein_spec.thickness)

# Capture video from your webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)

    # Process the image and draw landmarks
    results = hands.process(image)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            draw_vein_like_structure(image, hand_landmarks)
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, drawing_spec, vein_spec)

    # Display the image
    cv2.imshow('Hand Tracking', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()