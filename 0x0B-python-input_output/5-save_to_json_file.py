#!/usr/bin/python3
"""Save to Json File"""
import json


def save_to_json_file(my_obj, filename):
    """Save to Json File"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
