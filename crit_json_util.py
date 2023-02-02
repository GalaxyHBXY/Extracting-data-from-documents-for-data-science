import json


def get_crit_section(input_path='selected/Label.txt', output_path='critical_area.txt') -> None:
    '''
    Retrieve the manuelly labeled areas from the output text
    '''
    selected_list = []
    # iterate the list to find the coordinates of the critical areas
    with open(input_path) as f:
        for line in f:
            raw_json = line.split("\t")[1]
            data = json.loads(raw_json)
            for item in data:
                if item["key_cls"] != "None":
                    selected_list.append(item)
            
    # write to the output file
    with open(output_path, "w") as new_file:
        # convert it to json format
        text = json.dumps(selected_list)
        new_file.write(text)
