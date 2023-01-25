# CS31 - Extracting  data from documents for data science

#### 1. Introduction

This project aims to extract valuable information from the old scanned documents. 

#### 2. Installation

- Python3 environment
- Dependency installation: `pip3 install requirements.txt`





#### 3. Methodology

1. input a pdf file

2. convert it to a set of image files (a pdf file can have multiple pages), and save them to a temporary directory (`[root working directory]/tmp/`)

   1. time consuming - needs to find a trade-off between the efficiency and the image quality

3. iterate through the `.../tmp/` directory with the **template matching** script, the matched images are renamed and saved in `.../selected` directory.

4. clean `.../tmp/` and repeat 1-3.

5. pre-define the position of the critical areas by the labelling tool

   1. `json_util.py`

   2. `PPOCRLabel --kie True`

6. Running the OCR program on each image in `.../selected/` that retrieves the text in the certain area (nearest valid block).

7. save the outputs into a JSON file for further analysis

   1. ```json
      // sample format
      {
          name: "xxx",
          estate_of: "xxx",
          issue_date: "dd-mm-yyyy",
          date_of_death: "dd-mm-yyyy",
          total_tax_payment: 123,
          total_due: 123,
      }
      ```

   2. ```json
      // real output
      {
      'date_of_death': ('03-14-2010', 0.9969242215156555), 'total_tax_payment': ('6.036.00', 0.9693364500999451), 'total_due': ('.00', 0.9907954335212708),
      'name': ('JAMES J ZAYDON JR ESQ', 0.99156653881073), 'estate_of': ('REV-1547 EX AFP (12-09)', 0.9862002730369568)
      }  
      ```

#### Reference

- PaddleOCR GitHub Repo: https://github.com/PaddlePaddle/PaddleOCR