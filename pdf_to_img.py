from pdf2image import convert_from_path
import sys
import os


def pdf_to_img(file):

    # create folder
    super_path = "tmp"
    folder = os.path.exists(super_path)

    if not folder:                   
        os.makedirs(super_path)           

    pages = convert_from_path(file, 200)
    i = 0
    for page in pages:
        base_path = os.path.basename(file) + f"_{i}.jpg"
        temp_path = os.path.join(super_path, base_path)
        page.save(temp_path, 'JPEG')
        i += 1