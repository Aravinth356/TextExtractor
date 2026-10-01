import re

def name_extractor(file):
    with open(file, "r") as file:
        records = file.read()
        name_pattern = r"Name: