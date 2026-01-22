# Author: jiai27 (Joaquin Carbonell)
# Description:   used to pre-process images using openCV

#grayscaling, binarize, grid cells (known dimensions, work on unknown later), crop character images, resize to a fixed resolution
#refer to opencv repo
#intended input: an image with handwriting on it, real or online handwriting
#developing input: already segmented words, needs to be segmented to letters

#---dependencies---
import cv2 as cv
import numpy as np
print(cv.__version__)

<<<<<<< HEAD
import kagglehub as kg
# Download latest version
path = kg.dataset_download("nibinv23/iam-handwriting-word-database")
print("Path to dataset files:", path)


#key = KGAT_2bebedb4bff0533779c78bf4e6c3d1f5
kg.login()



#grayscaling, binarize, grid cells (known dimensions, work on unknown later), crop character images, resize to a fixed resolution
#refer to opencv repo for above

=======
#-------------------
#later development:

#word segmentation (sentence -> words), should return a list?

example_words = []


#grayscale & binarize
def gray_binarize(image):
    pass


def segment_image(image):
    pass
>>>>>>> 0a3e2bc125f1516fd9c56fd8a756028caf53a1f1
