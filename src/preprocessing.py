# Author: jiai27 (Joaquin Carbonell)
# Description:   used to pre-process images using openCV

import cv2 as cv
import numpy as np
print(cv.__version__)

import kagglehub as kg
# Download latest version
path = kg.dataset_download("nibinv23/iam-handwriting-word-database")
print("Path to dataset files:", path)


#key = KGAT_2bebedb4bff0533779c78bf4e6c3d1f5
kg.login()



#grayscaling, binarize, grid cells (known dimensions, work on unknown later), crop character images, resize to a fixed resolution
#refer to opencv repo for above

