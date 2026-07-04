#!/usr/bin/env python3
"""
Module to convert CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into a JSON file (data.json).
    Returns True if successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = list(reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
