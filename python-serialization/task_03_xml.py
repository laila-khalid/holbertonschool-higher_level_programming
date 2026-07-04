#!/usr/bin/env python3
"""
Module for serializing and deserializing dictionaries using XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to a file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8')


def deserialize_from_xml(filename):
    """
    Reads XML data from a file and returns a deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict
    except Exception:
        return None
