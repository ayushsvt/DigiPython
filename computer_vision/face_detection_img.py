import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

IMAGE_FILES = ['computer_vision/photo1.jpg']
with mp_face_detection.FaceDetection( model_selection=1, min_detection_confidence=0.5) as face_detection:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    image= cv2.resize(image,(640,480))
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if not results.detections:
      continue
    annotated_image = image.copy()
    for detection in results.detections:
        mp_drawing.draw_detection(annotated_image, detection)
    cv2.imshow('original',image)
    cv2.imshow('Face Dection',annotated_image)
    cv2.waitKey(0)
cv2.destroyAllWindows()
    
