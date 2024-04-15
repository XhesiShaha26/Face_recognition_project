import cv2

def detect_faces(image):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

def detect_face_orientation(faces, image_width):
    orientations = []
    for (x, y, w, h) in faces:
        face_center_x = x + w // 2
        if face_center_x < image_width // 3:
            orientation = "Turn head to the left"
        elif face_center_x > (2 * image_width) // 3:
            orientation = "Turn head to the right"
        else:
            orientation = "Face orientation is centered"
        orientations.append(orientation)
    return orientations

def draw_faces(image, faces, orientations):
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, orientations[i], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.imshow('Face Recognition', image)
    cv2.waitKey(1)