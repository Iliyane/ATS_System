# ATS_System
This system reads a PDF-File and extracts unstructured data and based on requirenments creates visualisations score for HR. 
# ATS Resume Screening System

An Automated Resume Screening (ATS) system that analyzes PDF resumes and scores candidates based on keywords relevant to various professional fields in industrial and systems engineering.

## Description

This Python-based tool extracts text from PDF resumes, performs text cleaning, and evaluates the content against predefined keyword dictionaries for different job areas. It generates a score for each field and visualizes the results in a pie chart, helping HR professionals quickly assess candidate suitability.

## Features

- **PDF Text Extraction**: Reads and extracts text from PDF resume files using PyPDF2
- **Text Cleaning**: Converts text to lowercase, removes numbers and punctuation
- **Keyword Matching**: Scores resumes against comprehensive keyword lists for 6 professional fields:
  - Quality Management
  - Operations Management
  - Supply Chain
  - Project Management
  - Data Analytics
  - Healthcare
- **Scoring Visualization**: Generates a pie chart showing the distribution of scores across fields
- **Results Export**: Saves the visualization as a PNG image

## Requirements

- Python 3.x
- PyPDF2
- textract
- pandas
- matplotlib
- re (built-in)
- string (built-in)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Iliyane/ATS_System.git
   cd ATS_System
   ```

2. Install the required Python packages:
   ```bash
   pip install PyPDF2 textract pandas matplotlib
   ```

   Note: textract may require additional system dependencies. On Ubuntu/Debian:
   ```bash
   sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig
   ```

## Usage

1. Place your resume PDF file in the project directory and name it `CV_pages.pdf`

2. Run the script:
   ```bash
   python resume_screening.py
   ```

3. The script will:
   - Extract and clean text from the PDF
   - Calculate scores for each professional field
   - Display the scores in the console
   - Generate and save a pie chart as `results.png`

## Example Output

The script outputs a pandas DataFrame with scores sorted by highest to lowest:

```
                      score
Data Analytics           15
Operations management    8
Project management       6
Supply chain             4
Quality                  3
Healthcare               1
```

And generates a pie chart visualization.

## Customization

- **Resume File**: Change the filename in the script if your PDF has a different name
- **Keyword Dictionary**: Modify the `english_dict` dictionary to add, remove, or update keywords for each field
- **Fields**: Add new professional fields by extending the dictionary and updating the scoring logic

## Author

Iliyana Kamenova

## License

This project is open-source. Please refer to the original article for any licensing considerations. 
