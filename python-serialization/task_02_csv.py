#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert CSV data into JSON format.

    Args:
        filename (str): Name of the CSV file

    Returns:
        bool: True if conversion succeeds, False otherwise
    """
    try:
        data = []

        with open(filename, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError):
        return False
