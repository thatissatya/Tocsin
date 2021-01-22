import tkinter as tk
from PIL import ImageTk, Image
from imutils import face_utils
from scipy.spatial import distance
from tkinter import Canvas, NW, END, messagebox
import time, cv2, dlib, pyautogui, os, datetime, pygame
from utils.changeStatus import * # for Different System modes.

def create_resource(ti=15, v="Hybernation", inac=5, asleep=2, fold="/home/satya/Pictures"):
    # Initialize Pygame and load music
    ft = 0
    pygame.mixer.init()
    pygame.mixer.music.load(r'assets\audio\faded.ogg')
    # Minimum threshold of eye aspect ratio below which alarm is triggerd
    EYE_ASPECT_RATIO_THRESHOLD = 0.3
    # Minimum consecutive frames for which eye ratio is below threshold for alarm to be triggered
    EYE_ASPECT_RATIO_CONSEC_FRAMES = 50
    # COunts no. of consecutuve frames below threshold value
    COUNTER = 0
    b = 1
    flag1 = True
    global inace
    # Load face cascade which will be used to draw a rectangle around detected faces.
    face_cascade = cv2.CascadeClassifier(r"assets\haarcascades\haarcascade_frontalface_default.xml")
    # This function calculates and return eye aspect ratio
    def eye_aspect_ratio(eye):
        A = distance.euclidean(eye[1], eye[5])
        B = distance.euclidean(eye[2], eye[4])
        C = distance.euclidean(eye[0], eye[3])
        # EAR = eye_aspect_ratio
        ear = (A + B) / (2 * C)
        return ear
    # Load face detector and predictor, uses dlib shape predictor file
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(r'assets\shape_predictor_68_face_landmarks.dat')
    # Extract indexes of facial landmarks for the left and right eye
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']
    # Start webcam video capture /Give some time for camera to initialize(not required) /time.sleep(2)
    a = 1
    while (True):
        video_capture = cv2.VideoCapture(0)
        nowt = datetime.datetime.now()
        nt1 = nowt.minute
        newt = nowt + datetime.timedelta(minutes=ti)
        nt2 = newt.minute
        print("***********")
        print(nowt, newt)
        print("***********")

        while (True):
            # Read each frame and flip it, and convert to grayscale
            ret, frame = video_capture.read()
            frame = cv2.flip(frame, 1)
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # Detect facial points through detector function
                faces = detector(gray, 0)
                # Detect faces through haarcascade_frontalface_default.xml
                face_rectangle = face_cascade.detectMultiScale(gray, 1.3, 5)
                # Draw rectangle around each face detected
                for (x, y, w, h) in face_rectangle:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # Detect facial points
                # print(type(faces))
                if len(faces) == 0:
                    COUNTER = 0
                    inacs = datetime.datetime.now()
                    # print(inacs)
                    if flag1:
                        inace = inacs + datetime.timedelta(minutes=inac)
                        inace = inace.minute
                        flag1 = False
                    if (inacs.minute > inace and b == 1 and flag1 == False):
                        pygame.mixer.music.play(-1)
                        b = 0
                    print(inacs, inace)
                    if (b == 0 and flag1 == False and inacs.minute > (inace + 1)):
                        flag1 = True
                        b = 1
                        pygame.mixer.music.stop()
                        pic = pyautogui.screenshot()
                        sour = fold + "screenshot.png"
                        pic.save(sour)
                        ft = 1
                for face in faces:
                    if (b != 1):
                        flag1 = True
                        b = 1
                        pygame.mixer.music.stop()
                    shape = predictor(gray, face)
                    shape = face_utils.shape_to_np(shape)
                    # Get array of coordinates of leftEye and rightEye
                    leftEye = shape[lStart:lEnd]
                    rightEye = shape[rStart:rEnd]
                    # Calculate aspect ratio of both eyes
                    leftEyeAspectRatio = eye_aspect_ratio(leftEye)
                    rightEyeAspectRatio = eye_aspect_ratio(rightEye)
                    eyeAspectRatio = (leftEyeAspectRatio + rightEyeAspectRatio) / 2
                    # Use hull to remove convex contour discrepencies and draw eye shape around eyes
                    leftEyeHull = cv2.convexHull(leftEye)
                    rightEyeHull = cv2.convexHull(rightEye)
                    cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                    cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
                    # Detect if eye aspect ratio is less than threshold
                    # print(eyeAspectRatio)
                    if (eyeAspectRatio < EYE_ASPECT_RATIO_THRESHOLD):
                        COUNTER += 1
                        # If no. of frames is greater than threshold frames,
                        print(COUNTER, EYE_ASPECT_RATIO_CONSEC_FRAMES)
                        if COUNTER >= EYE_ASPECT_RATIO_CONSEC_FRAMES and COUNTER >= asleep and a == 1:
                            pygame.mixer.music.play(-1)
                            a = 0
                            cv2.putText(frame, "You are Drowsy", (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255),
                                        2)
                        if COUNTER >= EYE_ASPECT_RATIO_CONSEC_FRAMES and COUNTER >= (asleep + 20):
                            pic = pyautogui.screenshot()
                            sour = fold + "screenshot.png"
                            pic.save(sour)
                            pygame.mixer.music.stop()
                            ft = 1
                            break
                    else:
                        pygame.mixer.music.stop()
                        a = 1
                        COUNTER = 0
                if ft == 1:
                    break
            cv2.imshow('Video', frame)
            kp = cv2.waitKey(1)
            nt1 = datetime.datetime.now().minute
            if (nt2 < nt1):
                break
            elif (kp & 0xFF == ord('q')):
                return
        if ft == 1:
            video_capture.release()
            cv2.destroyAllWindows()
            pygame.mixer.music.stop()
            break
        else:
            video_capture.release()
            cv2.destroyAllWindows()
            pygame.mixer.music.stop()
            time.sleep(60 * ti)
    if ft == 1:
        time.sleep(10)
        if v == "Hybernation":
            changeStatus.hybernation()
        else:
            changeStatus.shut_down()

