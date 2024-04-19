#Temp

#8-4 
#Reconhecimento OCR 
#Tensorflow, LM, DL, Mnisp e Kaglle

import tensorflow
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import zipfile
from tensorflow.keras.models import load_model
from imutils.contours import sort_contours
#import imutils
from google.colab.patches import cv2_imshow
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

