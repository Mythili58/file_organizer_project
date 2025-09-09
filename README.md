📂 Smart File Organizer

Smart File Organizer is a Python-based automation tool that helps you clean and structure your files effortlessly. It scans a given folder, extracts text from different file types, and organizes them into meaningful categories using keyword rules. It also detects and skips duplicate files.

✨ Features

🔍 Automatic Categorization – Organizes files (PDF, Word, Excel, CSV, PPT, TXT) into folders like Academics, Finance, Work, Health, Personal.

📑 Text Extraction – Reads file content using libraries like PyPDF2, python-docx, pandas, python-pptx.

🚫 Duplicate Detection – Avoids storing the same file twice (MD5 hash-based).

📊 Streamlit Dashboard – Simple web interface to select a folder and view results with summaries.

📂 Organized Output – Creates a structured organized/ folder with subcategories.

🛠️ Tech Stack

Language: Python

Libraries: pandas, python-docx, PyPDF2, python-pptx, openpyxl

UI: Streamlit (web-based interface)

🚀 How It Works

Enter or select a folder path in the Streamlit app.

The tool extracts text from each file and matches it with keywords from categories.json.

Files are moved into respective category folders (inside organized/).

Duplicates are detected and skipped.

A summary report is displayed in the UI.

📦 Installation
git clone https://github.com/your-username/smart-file-organizer.git
cd smart-file-organizer
pip install -r requirements.txt

▶️ Run the App
streamlit run gui.py

📂 Example Output
organized/
│
├── Academics/
│   └── assignment.docx
├── Finance/
│   └── bank_statement.pdf
├── Work/
│   └── meeting_notes.txt
└── Uncategorized/
    └── random_file.csv

📌 Future Enhancements

Add custom category creation via UI

Provide file preview before moving

Option to export summary report (CSV/Excel)
