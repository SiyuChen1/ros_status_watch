import re

def filter_digtal(string):
    result_list = re.findall(r"\d+\.?\d*",string)
    return result_list[-1]

