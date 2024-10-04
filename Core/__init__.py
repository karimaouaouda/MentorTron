"""
every embded system has two main functions, steup() and run()
setup() used to initialize the default values and variables for the system
run() is the main loop for the system
"""
from Core.models.FacialRecognition import detector

def setup():
    pass


def run():
    detector.start_detecting()