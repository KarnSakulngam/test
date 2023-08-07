import csv


class PoseTypeCollection:
    def __init__(self) -> None:
        self.header = ['pose','left_shoulder_x','left_shoulder_y', 'right_shoulder_x','right_shoulder_y', 'left_elbow_x','left_elbow_y','right_elbow_x','right_elbow_y','left_wrist_x','left_wrist_y','right_wrist_x','right_wrist_y','left_hip_x','left_hip_y','right_hip_x','right_hip_y','left_knee_x','left_knee_y','right_knee_x','right_knee_y','left_ankle_x','left_ankle_y','right_ankle_x','right_ankle_y']
        self.file = open('posetype.csv','w',encoding='UTF8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(self.header)

    def log(self,landmarks):
        datalist = ["A", landmarks[12].x*640, landmarks[12].y*480, landmarks[11].x*640,landmarks[11].y*480,landmarks[14].x*640,landmarks[14].y*480,landmarks[13].x*640,landmarks[13].y*480,landmarks[16].x*640,landmarks[16].y*480,landmarks[15].x*640,landmarks[15].y*480,landmarks[24].x*640,landmarks[24].y*480,landmarks[23].x*640,landmarks[23].y*480,landmarks[26].x*640,landmarks[26].y*480,landmarks[25].x*640,landmarks[25].y*480,landmarks[28].x*640,landmarks[28].y*480,landmarks[27].x*640,landmarks[27].y*480,]

        self.writer.writerow(datalist)

#List every coordinate given
#Go to Camera.py then import data and use the PoseTypeCollection class from data import.
#collection = PoseTypeCollection()
#collection.log(landmarks)
#Change path
#HW2: press 32 = pose A, Button B = pose B,....