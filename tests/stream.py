from deepface import DeepFace

# DeepFace.stream("dataset", enable_face_analysis=False, anti_spoofing=True)  # opencv
# DeepFace.stream("dataset", detector_backend = 'opencv', enable_face_analysis=False, anti_spoofing=True)
# DeepFace.stream("dataset", detector_backend = 'ssd', enable_face_analysis=False, anti_spoofing=True)
# DeepFace.stream("dataset", detector_backend='mtcnn', enable_face_analysis=False, anti_spoofing=True)
# DeepFace.stream("dataset", detector_backend='dlib', enable_face_analysis=False, anti_spoofing=True)
DeepFace.stream("dataset", detector_backend='retinaface', enable_face_analysis=False, anti_spoofing=True)
