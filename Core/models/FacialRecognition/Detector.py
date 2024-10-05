import cv2
import mediapipe as mp

class Detector():
    def __init__(self):
        self.mp_face = mp.solutions.face_detection
        self.drawings = mp.solutions.drawing_utils

        self.acquaintances = self.load_acquaintances() or []

        self.camera = cv2.VideoCapture(0)

    def load_acquaintances(self):
        return None


    def start_detection(self):
        mp_face_detection = mp.solutions.face_detection
        mp_drawing = mp.solutions.drawing_utils

        while self.camera.isOpened():
            success, image = self.camera.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self.mp_face.process(image)

            # Draw the face detection annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(image, detection)
                # Flip the image horizontally for a selfie-view display.
                cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break
        self.camera.release()


# For static images:
    # IMAGE_FILES = []
    # with mp_face_detection.FaceDetection(
    #         model_selection=1, min_detection_confidence=0.5) as face_detection:
    #     for idx, file in enumerate(IMAGE_FILES):
    #         image = cv2.imread(file)
    #         # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
    #         results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    #
    #         # Draw face detections of each face.
    #         if not results.detections:
    #             continue
    #         annotated_image = image.copy()
    #         for detection in results.detections:
    #             print('Nose tip:')
    #             print(mp_face_detection.get_key_point(
    #               detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
    #             mp_drawing.draw_detection(annotated_image, detection)
    #         cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)