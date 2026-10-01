# TextExtractor

A small open-source project for practising Git and GitHub collaboration.

`records.txt` contains messy, made-up customer records: names, phone numbers, email addresses, Aadhaar numbers, PAN numbers, PIN codes and dates, all mixed together. The goal of this project is to build a collection of **extractor functions** that use Python's `re` (regular expressions) module to pull each kind of information out of that file.

Each extractor is written by a different contributor, through a fork and a pull request.

> All data in `records.txt` is fictional and generated for practice only.

---

## Project files

| File | What it is |
|---|---|
| `README.md` | This guide |
| `requirements.txt` | Python packages needed |
| `records.txt` | The text to extract information from |
| `extract_<what>.py` | One file per contributor, added by pull request |

---

## Getting started

```bash
git clone https://github.com/<your-username>/TextExtractor.git
cd TextExtractor
pip install -r requirements.txt
```

---

## How to contribute

1. **Pick a task.** Go to the **Issues** tab, choose an open issue, and comment *"I'll take this"* so nobody else picks the same one.
2. **Fork** this repository to your own GitHub account.
3. **Clone your fork** (not this repository) to your laptop.
4. **Create a branch** named after your task:
```bash
   git checkout -b feature/phone
```
5. **Add one file** next to `records.txt`, named `extract_<what>.py`, for example `extract_phone.py`.
6. **Commit and push** to your fork:
```bash
   git add extract_phone.py
   git commit -m "Add phone number extractor"
   git push -u origin feature/phone
```
7. **Open a pull request** to this repository's `main` branch. In the description, write `Closes #<issue-number>`.

### Rules

- **One file, one function, one pull request.**
- Name the file `extract_<what>.py` and the function `extract_<what>`.
- Use only Python's built-in `re` module.
- The function takes the text as a string and returns a **list of matches**.
- Add a short docstring with **three example matches** from `records.txt`.

### Template

```python
import re


def extract_email(text):
    """Return all email addresses found in text.

    Examples from records.txt:
        priya.sharma@example.com
        rahul_k@mail.example.in
        support@shop.example.org
    """
    pattern = r"[\w.+-]+@[\w-]+\.[\w.-]+"
    return re.findall(pattern, text)


if __name__ == "__main__":
    with open("records.txt", encoding="utf-8") as f:
        print(extract_email(f.read()))
```

Run it with:

```bash
python extract_email.py
```

---

## Extractors

| What to extract | File | Status |
|---|---|---|
| Email addresses | `extract_email.py` | open |
| Phone numbers | `extract_phone.py` | open |
| Names | `extract_name.py` | open |
| Aadhaar numbers | `extract_aadhaar.py` | open |
| PAN numbers | `extract_pan.py` | open |
| PIN codes | `extract_pincode.py` | open |
| Dates | `extract_date.py` | open |

---

## Contributors

- Maintainer
