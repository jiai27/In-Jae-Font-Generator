# Author: jiai27 (Joaquin Carbonell)
# Description:   used to pre-process images using openCV
#                grayscaling, binarize, grid cells (known dimensions, work on unknown later), crop character images, resize to a fixed resolution
#                intended input: an image with handwriting on it, real or online handwriting
#                developing input: already segmented words, needs to be segmented to letters

'''
---some notes during dev---
- the words.txt file that comes with the IAM database contains data on binarizing threshold, bounding box coords, etc, use these to validate and not take it directly since regular inputs won't have this
'''

#---dependencies---
import cv2 as cv
import numpy as np

#-------------------
#later development section: word segmentation (sentence -> words), should return a list?
# deskewing should probably be done here so word processing has an easier time, deskewing 

#-------------------


#--WORD SEGMENTATION--; the assumed input is just a word, future proofing involves segmenting a sentence into a word
def main(): 
    #initialize some sample words
    image_path = "data/iam_words/words/"
    labour = cv.imread(image_path+"a01/a01-000u/a01-000u-01-03.png")                 #data regarding this image (from words.txt): a01-000u-01-03 ok 156 1400 937 294 59 NN Labour
    fearlessly = cv.imread(image_path+"b04/b04-010/b04-010-05-03.png")               #data regarding this image (from words.txt): b04-010-05-03 ok 172 1072 1656 434 106 RB fearlessly
    nationalists = cv.imread(image_path+"a02/a02-098/a02-098-04-01.png")             #data regarding this image (from words.txt): a02-098-04-01 err 162 640 1460 356 68 NNS nationalists
    blue = cv.imread("examples/ex1.png")

    example_words = [labour,fearlessly, nationalists, blue]
    for index, word in enumerate(example_words):
        #cv.imshow(f'orig word {index}',word)
        gray_normed = gray_norm(word)
        cv.imshow(f'gray word {index}',gray_normed)
        binarized = binarize(gray_normed)
        cv.imshow(f'binarized word {index}',binarized)
        #extracted = extract_characters(binarized)
        #cv.imshow(f'extracted word {index}', extracted)
    cv.waitKey(0)

    

def gray_norm(image):
    '''
    input: image of a word (image)
    function: grayscales, crops, normalizes image to proper size for all words
    '''
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    #resize to (hxw: 64x512 max)
    ratio = gray.shape[1] / gray.shape[0]   #width/height ratio

    #hard cap height at 64
    new_width = int(64 * ratio)    
    dimensions = (new_width,64) #width, height

    #resize accordingly
    resized = cv.resize(gray, dsize=dimensions, interpolation=cv.INTER_LINEAR)

    return resized

#binarize (thresholding)
def binarize(image, threshold=150):
    '''
    input: image of a word (image), threshold value (default is 100)
    function: binarizes the image, removes noise as well. choice of thresholding subject to change depending on data; 
    '''
    thsh_val, thresh = cv.threshold(image, threshold, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)   #even if thsh_val isn't used, it must be returned somewhere otherwise cv2.error 
    return thresh

def extract_characters(image):
    '''
    input: image of a word (image), assumed to already be grayscaled, resized and binarized
    function: 
    '''
    contours, hierarchy = cv.findContours(image,mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)
    #img = cv.drawContours(image, contours, -1, (0,255,0), 3)
    #print(type(contours), contours,"\n", type(hierarchy), hierarchy)
    return 

def segment_image(image):
    trans1 = gray_norm(image)
    trans2 = binarize(trans1)
    #trans3 = ()


    pass


if __name__ == "__main__":
    main()