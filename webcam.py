import cv2
from face_recognition import detect_faces, detect_face_orientation, draw_faces

def start_webcam():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        image_height, image_width, _ = frame.shape
        faces = detect_faces(frame)
        orientations = detect_face_orientation(faces, image_width)
        draw_faces(frame, faces, orientations)
        
        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
