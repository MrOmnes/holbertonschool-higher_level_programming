#!/usr/bin/python3
"""Load from a json file"""
import json


def load_from_json_file(filename):
    """Load from a json file"""
    with open(filename, "r") as f:
        try:
            return json.load(f)
        except Exception:
            return []
