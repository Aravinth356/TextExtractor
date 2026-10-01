import re

def phone_extract(file):
    with open('records.txt', 'r') as file:
        records = file.read()   #str object
        phone_pattern = r"phone:\s*(\+91\s?\d{10})"
        phones = re.findall(pattern=phone_pattern,string=records)
    return phones

print(phone_extract('records.txt'))