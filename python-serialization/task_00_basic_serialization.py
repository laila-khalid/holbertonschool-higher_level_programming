#!/usr/bin/env python3
"""
Module for basic serialization and deserialization using JSON.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Deserializes a JSON file to recreate a Python Dictionary.
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
