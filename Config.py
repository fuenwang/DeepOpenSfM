import os
import numpy as np

IMAGE_WIDTH = 1280
IMAGE_HEIGHT = 720

OPENSFM_PATH = '/home/Futen/OpenSfM'

DEEPMATCH_PATH = '/home/Futen/deepmatch/deepmatching'
DEEPMATCH_THREAD = 8

class Info:
    def __init__(self, path):
        self.path = path
        self.image_path = '%s/images'%path
        self.match_path = '%s/matches'%path
        self.match_tmp_path = '%s/matches_deep'%path 
    def ImageLst(self):
        return sorted(os.listdir(self.image_path))
    def PointFileName(self, img):
        return '%s/%s_points.npy'%(self.match_path, img)
    def LoadPointData(self, img):
        return np.load(self.PointFileName(img)).item()
