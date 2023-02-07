import pdf_to_img
import os
from filter_util import filter
from ocr_util import retrieve_critical_area, find_candidates, retrieve_info
from crit_json_util import get_crit_section

def step_0():
    print("step 0...")
    get_crit_section()


def step_1(path='target'):
    print("step 1...")
    for _,_,files in os.walk(path):
        for target_file in files:
            pdf_to_img.pdf_to_img(os.path.join(path, target_file))
            print(target_file)

def step_2(input_path, output_path, template_path):
    print("step 2...")
    filter(input_path, output_path, template_path)

def step_3(target_path, critical_area) -> list:
    print("step 3...")
    critical_area = retrieve_critical_area(critical_area)
    result_lst = []
    for _,_,i in os.walk(target_path):
        for image in i:
            print("processing " + image)
            lst = retrieve_info(os.path.join(target_path, image))
            result = find_candidates(critical_area, lst)
            result_lst.append(result)
    
    return result_lst

if __name__ == "__main__":

    '''
    0. Generate the critical area file
    (only needs to be run once)
    '''
    step_0()

    ''' 
    1. pdf to image
    split the pdf files and convent them into image files
    '''
    step_1("sample_set")

    '''
    2. Filtering the images with the given template.
    The matched images will be saved in the selected/ directory
    '''
    step_2("tmp", "sample_output", "source/logo_2005.png")

    '''
    3. Scaning the critical area of the images in the selected/ directory
    return a dict that contains all the chosen information 
    '''
    result = step_3('sample_output', "critical_area.txt")

    '''
    Output results
    '''
    print(result)


