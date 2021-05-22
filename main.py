import os
import jarvis
import face_recognizer

 
if __name__ == "__main__":
    name = face_recognizer.faceRecognizer()
    jarvis.wishMe(name)
    jarvis.listenCommand()

