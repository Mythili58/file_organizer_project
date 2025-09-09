📂 Smart File Organizer

A lightweight file management tool to automatically organize documents, spreadsheets, presentations, and images into structured folders. It reduces clutter and makes file access quick and efficient — all from a simple, user-friendly interface.

📄 Description

The Smart File Organizer is a Python-based solution for managing everyday files. It extracts text from multiple file formats and categorizes them into predefined groups such as Academics, Finance, Work, Health, and Personal. Duplicate files are detected and skipped, ensuring a clean and well-structured directory. With a simple Streamlit interface, organizing files becomes as easy as one click.

🎯 Objective

Automatically organize files into relevant category folders

Support multiple file formats (PDF, DOCX, TXT, Excel, CSV, PPTX, Images)

Ensure clean storage by detecting and skipping duplicates

Provide a user-friendly interface for quick access

⭐ Features

📂 Auto Categorization – Organizes files into structured folders

📑 Multi-Format Support – Works with documents, spreadsheets, presentations, and images

🔁 Duplicate Detection – Skips already existing files to avoid clutter

🖥️ Simple UI – Streamlit-based interface for easy folder selection and execution

⚡ Lightweight & Fast – Runs locally with minimal setup

🧱 Project Structure
smart_file_organizer/
│
├── gui.py               # Streamlit-based user interface
├── main.py              # Core file organization logic
├── extractors.py        # File text extraction functions
├── categories.json      # Predefined keyword-based categories
├── organized/           # Output folder (auto-created after run)
├── requirements.txt     # Dependencies list
└── README.md            # Project documentation

📊 Example Output
Input Folder (before organizing)
Documents/
│
├── invoice_jan.pdf
├── exam_notes.docx
├── shopping_list.txt
├── salary_slip.pdf
├── meeting_report.pptx

Output Folder (after organizing)
Documents/organized/
│
├── Finance/
│   ├── invoice_jan.pdf
│   ├── salary_slip.pdf
│
├── Academics/
│   ├── exam_notes.docx
│
├── Work/
│   ├── meeting_report.pptx
│
├── Personal/
│   ├── shopping_list.txt

🛠️ Tools & Technologies

Python – Core logic & automation

pandas, python-docx, PyPDF2, python-pptx – File handling and text extraction

Pillow & pytesseract – Image text extraction (OCR)

Streamlit – Interactive web-based GUI
