#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import cv2
import numpy as np
import os
import shutil

def search_returnPoint(img,template,template_size):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template_ = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(img_gray, template_,cv2.TM_CCOEFF_NORMED)

    # threshold (confidence)
    threshold = 0.5

    loc = np.where(result >= threshold)

    point = ()
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + template_size[1], pt[1] + + template_size[0]), (7, 249, 151), 2)
        point = pt
    if point==():
        return None,None,None
    return img,point[0]+ template_size[1] /2,point[1]

def filter(input_path="tmp/", output_path="selected/", template_path="source/logo_2005.png"):

    scale = 1
    template = cv2.imread(template_path) #logo template
    template = cv2.resize(template, (0, 0), fx=scale, fy=scale)
    template_size= template.shape[:2]


    # create output_path
    folder = os.path.exists(output_path)

    if not folder:                   
        os.makedirs(output_path)   

    for _,_,files in os.walk(input_path):
        for i in files:
            file_path = input_path + i
            img = cv2.imread(file_path)
            img = cv2.resize(img, (0, 0), fx=scale, fy=scale)
            img,x_,y_ = search_returnPoint(img,template,template_size)
            if(img is not None):
                print(f"matched! {i}")
                shutil.copy(file_path, output_path)


    # clear the temporary images in input_path
    for _,_,files in os.walk(input_path):
        for file in files:
            os.remove(input_path + file)
