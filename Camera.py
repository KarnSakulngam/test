import cv2 #import code
import mediapipe as mp

cam_port = 0 #camera selecter
cam = cv2.VideoCapture(cam_port)
# Initialize mediapipe pose class.
mp_pose = mp.solutions.pose

# Setup the Pose function for images - independently for the images standalone processing.
pose_image = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)

# Initialize mediapipe drawing class - to draw the landmarks points.
mp_drawing = mp.solutions.drawing_utils

while True:        
    ret, image = cam.read()    # camera collect image [image =  keep array of pixel of RGB] [ret = image collected successfully = True | image collected unsuccessfully = False]
    image_in_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #BGR --> RGB
    
    resultant = pose_image.process(image_in_RGB) # AI (Pose image) process image that was coverted to RGB (image_in_RGB) then output the coordinate (resultant)
    if resultant.pose_landmarks: # If ai detected the body position

        mp_drawing.draw_landmarks(image=image, landmark_list=resultant.pose_landmarks, # mp draw use to image (image) with the position in output of ai (resultant.pose_landmarks)
                                connections=mp_pose.POSE_CONNECTIONS,
                                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255,255,255), #Color of landmarl drawing
                                                                            thickness=2, circle_radius=3),
                                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0,0,255), #Color of Line Connect dot
                                                                            thickness=4, circle_radius=2))
        cv2.imshow("GeeksForGeeks", image)    
        key = cv2.waitKey(1)

        if key == 32:
            pose_coordinate = [(resultant.pose_landmarks.landmark[11].x*640, resultant.pose_landmarks.landmark[11].y*480),
                               (resultant.pose_landmarks.landmark[12].x*640, resultant.pose_landmarks.landmark[12].y*480),
                               (resultant.pose_landmarks.landmark[13].x*640, resultant.pose_landmarks.landmark[13].y*480),
                               (resultant.pose_landmarks.landmark[14].x*640, resultant.pose_landmarks.landmark[14].y*480),
                               (resultant.pose_landmarks.landmark[15].x*640, resultant.pose_landmarks.landmark[15].y*480),
                               (resultant.pose_landmarks.landmark[16].x*640, resultant.pose_landmarks.landmark[16].y*480),
                               (resultant.pose_landmarks.landmark[23].x*640, resultant.pose_landmarks.landmark[23].y*480),
                               (resultant.pose_landmarks.landmark[24].x*640, resultant.pose_landmarks.landmark[24].y*480),
                               (resultant.pose_landmarks.landmark[25].x*640, resultant.pose_landmarks.landmark[25].y*480),
                               (resultant.pose_landmarks.landmark[26].x*640, resultant.pose_landmarks.landmark[26].y*480),
                               (resultant.pose_landmarks.landmark[27].x*640, resultant.pose_landmarks.landmark[27].y*480),
                               (resultant.pose_landmarks.landmark[28].x*640, resultant.pose_landmarks.landmark[28].y*480)]
            print(pose_coordinate) 
    else:
        print('Error occured, please try again')    