from json import JSONDecoder, JSONDecodeError
import re
import shutil

NOT_WHITESPACE = re.compile(r'\S')

def decode_stacked(document, pos=0, decoder=JSONDecoder()):
    while True:
        match = NOT_WHITESPACE.search(document, pos)
        if not match:
            return
        pos = match.start()
        
        try:
            obj, pos = decoder.raw_decode(document, pos)
        except JSONDecodeError:
            # do something sensible if there's some error
            raise
        yield obj


def read_metadata(md_path, target_path, feature="REV 1547 NOTICE INH TAX APPRAISEMENT") -> None:

    '''
    Read the .out file and copy the target documents to a directory
    '''
    with open(md_path,encoding='utf-8-sig') as f:
        s = f.read()

    pdf_lst = []

    for obj in decode_stacked(s):
        # retrieve the dockets
        # **Modify this line if neccessary**
        dockets_list = obj["subinfo"]["sub-dockets"]["dockets"]

        for docket in dockets_list:
            if "content" in docket:
                # check if the document is the one we want
                tmp_doc = docket["content"]["description"]
                if feature in tmp_doc:
                    pdf_lst.append(docket["content"]["pdf"])
                        

    print(pdf_lst)
    for i in pdf_lst:
        shutil.copy(i, target_path)