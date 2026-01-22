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


#-------------------
#later development:

#word segmentation (sentence -> words), should return a list?

example_words = []


#grayscale & binarize
def gray_binarize(image):
    pass


def segment_image(image):
    pass
