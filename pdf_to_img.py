from pdf2image import convert_from_path
import sys
import os


def pdf_to_img(file):

    # create folder
    path = "tmp"
    folder = os.path.exists(path)

    if not folder:                   
        os.makedirs(path)           

    pages = convert_from_path(file, 200)
    i = 0
    for page in pages:
        page.save(f'tmp/{os.path.basename(file)}_{i}.jpg', 'JPEG')
        i += 1