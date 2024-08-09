""""""
import json, os
from standars import varnames as vnames

def get_file_groups(path:str)->dict:
    """
    This function returns the groups from a file.
    """
    with open(path, 'r') as f:
        data = json.load(f)
    return data

def get_utils_groups()->dict:
    """
    This function returns the groups from the utils.
    """
    pass
    

def get_group_id(body: dict)->int:
    """
    This function returns the group_id from the body.
    """
    