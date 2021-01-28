# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:23:15 2021

@author: Jake Taylor
"""
'''
import torch, torchvision
import torch
assert torch.__version__.startswith("1.7")
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()
import numpy as np
import os, json, cv2, random
from google.colab.patches import cv2_imshow
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
'''
import pickle
import detectron2
import torch


# Function that retrieves a standard dataset compatible with detectron2
def get_dict(type):
  """
  Returns a list[dict] containing information about the dataset
  
  """
  root = 'G:/My Drive/SSDD/datasets/' + type + '/'
  with open(root + "standardDict.pkl", "rb") as input_file:
    return pickle.load(input_file)










def main():
    get_dict('test')




if __name__ == '__main__':
    main()