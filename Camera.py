import csv
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

class PoseTypeCollection:
    def __init__(self) -> None:
        self.header = ['pose','left_shoulder_x','left_shoulder_y', 'right_shoulder_x','right_shoulder_y', 'left_elbow_x','left_elbow_y','right_elbow_x','right_elbow_y','left_wrist_x','left_wrist_y','right_wrist_x','right_wrist_y','left_hip_x','left_hip_y','right_hip_x','right_hip_y','left_knee_x','left_knee_y','right_knee_x','right_knee_y','left_ankle_x','left_ankle_y','right_ankle_x','right_ankle_y']
        self.file = open('posetype.csv','w',encoding='UTF8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(self.header)

    def log(self,landmarks):
        datalist = ["A", landmarks[12].x*640, landmarks[12].y*480, landmarks[11].x*640,landmarks[11].y*480,landmarks[14].x*640,landmarks[14].y*480,landmarks[13].x*640,landmarks[13].y*480,landmarks[16].x*640,landmarks[16].y*480,landmarks[15].x*640,landmarks[15].y*480,landmarks[24].x*640,landmarks[24].y*480,landmarks[23].x*640,landmarks[23].y*480,landmarks[26].x*640,landmarks[26].y*480,landmarks[25].x*640,landmarks[25].y*480,landmarks[28].x*640,landmarks[28].y*480,landmarks[27].x*640,landmarks[27].y*480,]

        self.writer.writerow(datalist)

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

        if key == 97:
            pose_coordinate = [(resultant.pose_landmarks.landmark[12].x*640, resultant.pose_landmarks.landmark[12].y*480),]
            print("The Coordinate of pose A is",pose_coordinate)
        elif key == 98:
            pose_coordinate = [(resultant.pose_landmarks.landmark[11].x*640, resultant.pose_landmarks.landmark[11].y*480),]
            print("The Coordinate of pose B is",pose_coordinate)
        elif key == 99:
            pose_coordinate = [(resultant.pose_landmarks.landmark[14].x*640, resultant.pose_landmarks.landmark[14].y*480),]
            print("The Coordinate of pose C is",pose_coordinate)
        elif key == 100:
            pose_coordinate = [(resultant.pose_landmarks.landmark[13].x*640, resultant.pose_landmarks.landmark[13].y*480),]
            print("The Coordinate of pose D is",pose_coordinate)
        elif key == 101:
            pose_coordinate = [(resultant.pose_landmarks.landmark[16].x*640, resultant.pose_landmarks.landmark[16].y*480),]
            print("The Coordinate of pose E is",pose_coordinate)
        elif key == 102:
            pose_coordinate = [(resultant.pose_landmarks.landmark[15].x*640, resultant.pose_landmarks.landmark[15].y*480),]
            print("The Coordinate of pose F is",pose_coordinate)
        elif key == 103:
            pose_coordinate = [(resultant.pose_landmarks.landmark[24].x*640, resultant.pose_landmarks.landmark[24].y*480),]
            print("The Coordinate of pose G is",pose_coordinate)
        elif key == 104:
            pose_coordinate = [(resultant.pose_landmarks.landmark[23].x*640, resultant.pose_landmarks.landmark[23].y*480),]
            print("The Coordinate of pose H is",pose_coordinate)
        elif key == 105:
            pose_coordinate = [(resultant.pose_landmarks.landmark[26].x*640, resultant.pose_landmarks.landmark[26].y*480),]
            print("The Coordinate of pose I is",pose_coordinate)
        elif key == 106:
            pose_coordinate = [(resultant.pose_landmarks.landmark[25].x*640, resultant.pose_landmarks.landmark[25].y*480),]
            print("The Coordinate of pose J is",pose_coordinate)
        elif key == 107:
            pose_coordinate = [(resultant.pose_landmarks.landmark[28].x*640, resultant.pose_landmarks.landmark[28].y*480),]
            print("The Coordinate of pose K is",pose_coordinate)
        elif key == 108:
            pose_coordinate = [(resultant.pose_landmarks.landmark[27].x*640, resultant.pose_landmarks.landmark[27].y*480),]
            print("The Coordinate of pose L is",pose_coordinate)

    else:
        print('Error occured, please try again')    