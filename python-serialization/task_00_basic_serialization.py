#!/usr/bin/env python3
"""
Module for basic JSON serialization and deserialization.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): Dictionary to serialize.
        filename (str): Name of the JSON file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file.

    Args:
        filename (str): Name of the JSON file.

    Returns:
        dict: Deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
