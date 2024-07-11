import json
import numpy as np
from typing import NamedTuple
from util_trans import *
import os


class visAnyCamera(NamedTuple):
    P_c2w: np.array  # 4x4
    K: np.array  # 3x3
    FovY: np.array  # radian
    FovX: np.array  # radian
    image_path: str
    image_name: str  # without .png/.jpg
    width: int
    height: int

    def to_dict(self):
        return {
            'P_c2w': self.P_c2w.tolist(),
            'K': self.K.tolist(),
            'FovX': self.FovX,
            'FovY': self.FovY,
            'image_path': self.image_path,
            'image_name': self.image_name,
            'width': self.width,
            'height': self.height
        }


def dic_to_camera(camera_dic):
    return visAnyCamera(
        P_c2w=np.array(camera_dic['P_c2w']),
        K=np.array(camera_dic['K']),
        FovX=np.array(camera_dic['FovX']),
        FovY=np.array(camera_dic['FovY']),
        image_path=camera_dic['image_path'],
        image_name=camera_dic['image_name'],
        width=camera_dic['width'],
        height=camera_dic['height'],
    )


class visAnyCameraList():
    def __init__(self, coordsys='cv'):
        self.all_camera_list = []
        self.coordsys = coordsys
        print(f'init visAnyCameraList, system is {self.coordsys}')

    def __len__(self):
        return len(self.all_camera_list)

    def get_camera_list(self):
        return self.all_camera_list

    def get_camera_dic_list(self):
        dic_list = [cam.to_dict() for cam in self.all_camera_list]
        return dic_list

    def add_camera(self, camera_info):
        self.all_camera_list.append(camera_info)

    def sort_cam(self):
        self.all_camera_list = sorted(self.all_camera_list.copy(), key=lambda x: x.image_name)

    def trans_cv_2_gl(self):
        if self.coordsys == 'cv':
            for camera in self.all_camera_list:
                camera.P_c2w = cv_2_gl(camera.P_c2w)
        else:
            raise Exception('current camera system is not cv')
        self.coordsys = 'gl'

    def trans_gl_2_cv(self):
        if self.coordsys == 'gl':
            for camera in self.all_camera_list:
                camera.P_c2w = gl_2_cv(camera.P_c2w)
        else:
            raise Exception('current camera system is not gl')
        self.coordsys = 'cv'

    def read_from_json(self, json_path, json_name='camera_info_opencv.json'):
        if self.coordsys != 'cv':
            raise Exception('current system is not cv, can not read')
        json_path = os.path.join(json_path, json_name)
        if not os.path.exists(json_path):
            raise Exception(f'not exist json file {json_path}')
        with open(json_path, 'r') as f:
            dic_list = json.load(f)
        self.all_camera_list = [dic_to_camera(cam_dic) for cam_dic in dic_list]

    def save_to_json(self, target_path, target_name='camera_info_opencv.json'):
        if self.coordsys != 'cv':
            raise Exception('current system is not cv, can not save')
        target_path = os.path.join(target_path, target_name)
        dic_list = self.get_camera_dic_list()
        with open(target_path, 'w') as f:
            json.dump(dic_list, f, indent=4)
        print(f'successfully saved to {target_path}')
