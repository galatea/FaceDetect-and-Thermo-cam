
import cv2
import dlib
import random

# Load the detector
detector = dlib.get_frontal_face_detector()

# Load the predictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# read the image
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    # Convert image into grayscale
    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

    # Use detector to find landmarks
    faces = detector(gray)

    for face in faces:
        x1 = face.left()  # left point
        y1 = face.top()  # top point
        x2 = face.right()  # right point
        y2 = face.bottom()  # bottom point
        celz = random.uniform(35.5, 43)

        # Create landmark object
        landmarks = predictor(image=gray, box=face)

        # Loop through all the points
        for n in range(27, 28):  #0-68
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            if celz>37.8:
                cv2.putText(img=frame, text="+" + str("{:.2f}".format(celz)), org=(x-26,y-10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(0, 0, 255), thickness=1)
                cv2.putText(img=frame, text="Covid gyanu!", org=(0,40), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255), thickness=1)       
            if celz<37.8:
                cv2.putText(img=frame, text="+" + str("{:.2f}".format(celz)), org=(x-26,y-10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(0, 255, 0), thickness=1)
                cv2.putText(img=frame, text="Irany a suli!", org=(0,35), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0), thickness=1)       
                                
    cv2.imshow(winname="CovidCam", mat=frame)            
 
    # show the image



    # Exit when escape is pressed
    if cv2.waitKey(delay=1) == 27:
        break

# When everything done, release the video capture and video write objects
cap.release()

# Close all windows
cv2.destroyAllWindows()