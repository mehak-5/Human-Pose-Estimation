import cv2
import mediapipe as mp

# Initialize Mediapipe pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Load an image
image_path = "mahi.png"
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Perform pose estimation
results = pose.process(image_rgb)

# Drawing landmarks only (no lines)
if results.pose_landmarks:
    print("Pose landmarks detected!")
    # Extract landmark data
    for idx, landmark in enumerate(results.pose_landmarks.landmark):
        print(f"Landmark {idx}: (x: {landmark.x}, y: {landmark.y}, z: {landmark.z})")
        
        # Get image dimensions
        h, w, c = image.shape
        
        # Convert normalized coordinates to pixel coordinates
        cx, cy = int(landmark.x * w), int(landmark.y * h)
        
        # Draw the keypoints (green color, filled circle)
        cv2.circle(image, (cx, cy), 5, (0, 255, 0), -1)

# Optional: Draw landmarks on the image (including connections)
annotated_image = image.copy()  # Corrected by adding parentheses to copy
mp_drawing.draw_landmarks(
    annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
)

# Display the output image
cv2.imshow("Pose Landmarks", annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Release resources
pose.close()
