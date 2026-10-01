import re

def age_extractor(file):
    with open('records.txt', 'r') as f:
        records = f.read()
        age_pattern = r'Age: (\d{2})'
        ages = re.findall(pattern=age_pattern, string=records)
        ages_int = list(map(lambda age: int(age), ages))
    return ages_int

if __name__ == "__main__":
    print(age_extractor('records.txt'))