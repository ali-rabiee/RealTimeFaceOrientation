import cv2
import dlib
import numpy as np
import math

def main(args=None):
    # Initialize face detector and landmark predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        for face in faces:
            landmarks = predictor(gray, face)
            
            # Draw all landmarks as red circles
            for n in range(0, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

            landmark_top_nose = (landmarks.part(27).x, landmarks.part(27).y)  # landmark 27
            landmark_bottom_nose = (landmarks.part(30).x, landmarks.part(30).y)  # landmark 30
            
            # Draw line between top and bottom of the nose
            cv2.line(frame, landmark_top_nose, landmark_bottom_nose, (255, 0, 0), 2)

            # Calculate the angle of the nose line
            nose_angle = math.degrees(math.atan2(landmark_bottom_nose[1] - landmark_top_nose[1], landmark_bottom_nose[0] - landmark_top_nose[0]))
            
            # Determine head orientation based on the nose angle
            if 80 <= abs(nose_angle) <= 100:  # Adjusted the range for neutral orientation
                orientation = "Neutral"
            elif abs(nose_angle) < 80:
                orientation = "Right"
            elif abs(nose_angle) > 100:
                orientation = "Left"

            # Display the orientation on the frame
            cv2.putText(frame, orientation, (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
