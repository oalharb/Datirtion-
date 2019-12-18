
import cv2
import os
from skimage import color, data, io, measure
from skimage.filters import threshold_otsu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from tqdm import tqdm
import glob
import matplotlib.image as mpimg
import seaborn as sns

mpl.rcParams['image.cmap'] = 'gray'
plt.rcParams['figure.dpi']= 300 #UPDATED
plt.rc("savefig", dpi=300) #UPDATED

def sort_contours(cnts, method="left-to-right"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = False

    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "right-to-left":
        i = 1

    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
        key=lambda b:b[1][i], reverse=reverse))

    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)
    
def image_crop(path):
    
    images = []
    counter = 1
    for img_path in tqdm(glob.glob(path)):

        img = cv2.imread(img_path,0)
        (thresh, img_bin) = cv2.threshold(img, 240, 255,cv2.THRESH_OTSU| cv2.ADAPTIVE_THRESH_GAUSSIAN_C) # UPDATE
        img_bin = 255-img_bin

        # Defining a kernel length
        global horizontal_lines_img, verticle_lines_img, kernel
        kernel_length = np.array(img).shape[1]//255

        # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
        verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
        # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
        hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))

        # Morphological operation to detect vertical lines from an image
        img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=1)
        verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=1)
        cv2.imwrite("verticle_lines.jpg",verticle_lines_img)
        # Morphological operation to detect horizontal lines from an image
        img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=1)
        horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=1)
        ###plt.subplot(1, 2, 1)  # 2 rows, 2 columns, 1st subplot = top left
        ###plt.imshow(verticle_lines_img);
        ###plt.axis('off')

        ###plt.subplot(1, 2, 2)  # 2 rows, 2 columns, 2nd subplot = top right
        plt.imshow(horizontal_lines_img);
        plt.axis('off')
        
        alpha = 1.0
        beta =  0.9 - alpha #UPDATE
        # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
        img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.5)
        (thresh, img_final_bin) = cv2.threshold(img_final_bin, 230,255, cv2.THRESH_OTSU| cv2.ADAPTIVE_THRESH_GAUSSIAN_C) # UPDATE
        plt.axis('off')
        plt.imshow(img_final_bin)

        # Find contours for image, which will detect all the boxes (if you are using Mac OX, delete im2,)
        im2, contours, hierarchy = cv2.findContours(img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #UPDATE

        # Sort all the contours by top to bottom.
        (contours, boundingBoxes) = sort_contours(contours, method="top-to-bottom")
        idx = 1

        for c in (contours):
            # Returns the location and width,height for every contour
            x, y, w, h = cv2.boundingRect(c)

    # If the box height is greater then 20, widht is >80, then only save it as a box in "cropped/" folder.
            if (w > 160 and h > 80) and w < 2.5 *h:
                idx += 3
                new_img = img[y:y+h, x:x+w]
                #plt.subplot(2,3, idx)
                plt.imshow(new_img)
                plt.axis('off')
                file_n = img_path.split('_')[-1].split('.')[0]
                plt.savefig(f'./cropped/{file_n}_Nutritions_{counter}.jpg',dpi=300) #UPDATED
                counter+=1
        #break    
