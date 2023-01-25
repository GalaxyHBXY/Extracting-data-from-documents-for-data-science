from paddleocr import PaddleOCR
import json
import os
import numpy as np
import cv2
import ast
import math
import sys


def retrieve_info(img_path:str) -> list:
    """
    Return a list of raw data for the OCR detection module
    """
    ocr = PaddleOCR(use_angle_cls=True, lang="en",show_log = False)
    result = ocr.ocr(img_path, cls=True)
    # for idx in range(len(result)):
    #     res = result[idx]
    return result


def retrieve_critical_area(file_path:str) -> dict:
    """
    Return a dict that contains the position of the critical area
    key: a string of the name of the critical section
    value: a list of coordinate
    """
    critical_area = {}
    with open(file_path) as f:
        tmp_dict = json.loads(f.read())
        for item in tmp_dict:
            tmp_key = item["key_cls"]
            tep_val = item["points"]
            critical_area[tmp_key] = tep_val
    return critical_area


def find_distance(template:list, candidate:list)-> float:
    """
    Return a float that represents the sum of the distance between the 
    four coordinates of the selected critical area and the scanned rectangle
    """
    distance_sum = 0
    for i,j in zip(template, candidate):
        distance = (float(i[0]) - float(j[0])) ** 2 + (float(i[1])- float(j[1])) ** 2
        distance_sum += distance
    return distance_sum
        
def find_candidates(critical_area:dict, raw_data:list) -> dict:
    """
    Iterativly compare each candidate in the raw data and find the most suitable item.
    Return a dictionary that records the critical areas' names as keys and 
    the corresponding items as values
    """
    result_dict = {}
    result_list = []
    key_names = []
    flatten_list = []
    # init the dict 
    for i in critical_area.keys():
        result_dict[i] = None
        result_list.append(sys.maxsize * 2 + 1)
        key_names.append(i)
        flatten_list.append(critical_area[i])

    for item in raw_data[0]:
        # compare the cooridate to each matrix
        coordinates = item[0]
        for idx, j in enumerate(flatten_list):
            tmp_dist = find_distance(coordinates, j)
            # compare with the best record
            if tmp_dist < result_list[idx]:
                result_list[idx] = tmp_dist
                result_dict[key_names[idx]] = item[1]
    print(result_dict)
    return result_dict




if __name__ == "__main__":
    with open('raw_data.txt') as f:
        raw_data = ast.literal_eval(f.read())
    # lst = retrieve_info("source/sample4.jpg")
    critical_area = retrieve_critical_area("critical_area.txt")
    find_candidates(critical_area, raw_data)

