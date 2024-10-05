"""
every embded system has two main functions, steup() and run()
setup() used to initialize the default values and variables for the system
run() is the main loop for the system
"""
from Core.models.FacialRecognition.Detector import Detector as FaceDetector
from multiprocessing import Process, Pool

#here you will define constants and variables, this is the setup

def start_detection(detector: FaceDetector) -> int :
    detector.start_detection()
    return 1

# TODO fix the pickle error

def run():
    face_detector = FaceDetector()

    face_detection_process = Process(target=start_detection, args=(face_detector,))

    face_detection_process.start()

    face_detection_process.join()