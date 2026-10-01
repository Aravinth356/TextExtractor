import re

def email_extractors(file):
    with open("records.txt",'r') as file:
        records = file.read()
        email_pattern = r"[a-z0-9._-]+@[\w]+\.[\w]+"
        emails = re.findall(pattern=email_pattern, string = records)
        return emails
                                    