# LS-SSDD-v1.0-ShipDetectionComputerVision
 
This is the code repository for the paper _Small Vessel Detection from Synthetic Aperture Radar (SAR) Imagery using Deep Learning_ .

Given the numerous models under consideration and the modular data downloading process, we present our code through interactive Jupyter notebooks.
Note that model weights, model output, and the dataset are *not* in this repo. The original dataset can be found at:
https://github.com/TianwenZhang0825/LS-SSDD-v1.0-OPEN

## Overview
The root directory features two notebooks training our best model and also performing inference.
'final_model.ipynb' is where we train the Improved model
'final_evaluation.ipynb' is where we perform inference on the Improved model

### class documents
Contains our papers as part of the CS230 Deep Learning.

### papers
Collection of papers that we used in the course of this project

### train
All of our training notebooks (which include baselines, experiments, and our final models presented in our paper)

### data 
Notebooks for preprocessing data and converting into 'Detectron2' format

### util
Notebooks for generating plots for the writeup and developing the sea-land mask for copy-paste augmentation using Otsu's method

### eval
Notebooks for evaluating our models

