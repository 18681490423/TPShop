import yaml
import inspect


def analyze_data(key):

    # search_data
    file_name = inspect.stack()[1].filename
    start_index = file_name.rfind("_")
    end_index = file_name.rfind(".")
    file_name = file_name[start_index + 1: end_index] + "_data"

    print(file_name)

    with open("./data/" + file_name + ".yml", 'r') as f:
        data = yaml.load(f)
        script_data = data[key]
        script_list = list()
        for i in script_data.values():
            script_list.append(i)
        return script_list

