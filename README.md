# Research Paper Evaluator

Research Paper Evaluator is a Python-based tool designed to fetch, process, and analyze research papers in PDF format from Google Drive using modular code. The project integrates Google Drive APIs, PDF processing, and LangGraph for advanced document analysis, saving the results to a CSV file.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Modules](#modules)
  - [Authenticate Drive](#authenticate-drive)
  - [PDF Fetcher](#pdf-fetcher)
  - [Processor](#processor)
- [Output](#output)
- [License](#license)

---

## Features
- **Google Drive Integration**: Fetch PDF files from a specified folder in Google Drive.
- **PDF Processing**: Extract content from PDFs and analyze it using LangGraph.
- **Error Handling**: Handle malformed PDFs, text extraction failures, and empty results gracefully.
- **Results Export**: Save analysis results to a structured CSV file.

---

## Project Structure

```
├── dist
├── csv_data
├── data
├── exp
├── src
│   ├── __pycache__
│   ├── __init__.py
│   ├── Authenticate_drive.py
│   ├── Pdf_fetcher.py
│   ├── process.py
├── .env
├── .gitignore
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
├── results.csv
```

- **`dist/`**: Compiled files (if applicable).
- **`csv_data/`**: Directory for storing intermediate CSV files.
- **`data/`**: Directory for storing downloaded PDFs.
- **`exp/`**: Experimental files or logs.
- **`src/`**: Main source code modules.
  - `Authenticate_drive.py`: Handles authentication with Google Drive.
  - `Pdf_fetcher.py`: Fetches and downloads PDFs from Google Drive.
  - `process.py`: Processes PDFs and analyzes them with LangGraph.
- **`.env`**: Environment variables (API keys, tokens, etc.).
- **`.gitignore`**: Specifies ignored files (e.g., `.env`).
- **`main.py`**: Main script for running the application.
- **`requirements.txt`**: Python dependencies.
- **`results.csv`**: Output CSV file containing analysis results.

---

## Requirements

- Python 3.8 or higher
- A Google Cloud Project with the Drive API enabled
- LangGraph for document analysis

Install the Python dependencies using:

```bash
pip install -r requirements.txt
```

---

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/research-paper-evaluator.git
   cd research-paper-evaluator
   ```

2. **Google Drive Authentication**:
   - Set up a Google Cloud project and enable the Google Drive API.
   - Download the `client_secrets.json` file and place it in the project directory.

3. **Environment Variables**:
   - Create a `.env` file with the following content:
     ```
     GOOGLE_API_KEY=<your-google-api-key>
     FOLDER_ID=<your-drive-folder-id>
     ```

4. **Run the Application**:
   Execute the `main.py` script:
   ```bash
   python main.py
   ```

---

## Usage

### Main Script
The main entry point is `main.py`, which orchestrates all modules:
1. Authenticates with Google Drive.
2. Fetches PDFs from the specified folder.
3. Processes the PDFs using LangGraph.
4. Saves results to `results.csv`.

---

## Modules

### Authenticate Drive
Located in `src/Authenticate_drive.py`.

Handles authentication with Google Drive using the Google Drive API.

### PDF Fetcher
Located in `src/Pdf_fetcher.py`.

Fetches all PDF files from a specified folder in Google Drive and downloads them to the `data/` directory.

### Processor
Located in `src/process.py`.

Processes each PDF to:
1. Extract text content using `PyPDFLoader`.
2. Analyze the content with LangGraph.
3. Save results to a CSV file.

---

## Output
The results are saved in `results.csv` with the following columns:
- **File**: Name of the PDF file.
- **Result**: Analysis result or error message.

Example:
```
File,Result
P001.pdf,Yes/No
P002.pdf,Error: Empty text
```

---

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

Let me know if you'd like to modify or add anything!