import os
import shutil
import json
import hashlib
from extractors import *

# Load categories
with open("categories.json", "r") as f:
    CATEGORIES = json.load(f)

CATEGORY_LIST = list(CATEGORIES.keys())

# Duplicate detection
hashes = set()
def is_duplicate(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    if file_hash in hashes:
        return True
    hashes.add(file_hash)
    return False

# Detect category (simple keyword matching)
def detect_category(text):
    text_lower = text.lower()
    for category, keywords in CATEGORIES.items():
        for word in keywords:
            if word in text_lower:
                return category
    return "Uncategorized"

# Organize folder
def organize_files(folder_path):
    organized_path = os.path.join(folder_path, "organized")
    os.makedirs(organized_path, exist_ok=True)

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    results = {"moved": [], "duplicates": [], "failed": []}

    for filename in files:
        file_path = os.path.join(folder_path, filename)

        if is_duplicate(file_path):
            results["duplicates"].append(filename)
            continue

        # Extract text
        text = ""
        ext = filename.lower()
        if ext.endswith(".txt"):
            text = extract_text_txt(file_path)
        elif ext.endswith(".docx"):
            text = extract_text_docx(file_path)
        elif ext.endswith(".pdf"):
            text = extract_text_pdf(file_path)
        elif ext.endswith(".xlsx"):
            text = extract_text_xlsx(file_path)
        elif ext.endswith(".csv"):
            text = extract_text_csv(file_path)
        elif ext.endswith(".pptx"):
            text = extract_text_pptx(file_path)

        # Detect category
        category = detect_category(text)

        # Create folder and move file
        cat_folder = os.path.join(organized_path, category)
        os.makedirs(cat_folder, exist_ok=True)
        try:
            shutil.move(file_path, os.path.join(cat_folder, filename))
            results["moved"].append((filename, category))
        except Exception as e:
            results["failed"].append((filename, str(e)))

    return results
