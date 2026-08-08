# 📜 Telugu OCR Text Extraction

> **A Telugu document OCR system that converts PDF documents into editable Telugu text using Tesseract OCR, OpenCV-based image preprocessing, and a Gradio web interface.**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv)
![Tesseract](https://img.shields.io/badge/Tesseract-Telugu%20OCR-4285F4?style=for-the-badge)
![Gradio](https://img.shields.io/badge/Gradio-Interface-FF7C00?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge&logo=numpy)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

---

## 📖 Overview

Telugu documents are often available as scanned PDFs or image-based documents where the text cannot be directly edited or searched.

This project provides an OCR-based workflow for extracting Telugu text from PDF documents. The system converts PDF pages into images, applies image preprocessing techniques using OpenCV, and uses Tesseract OCR with Telugu language support to extract the text.

A Gradio-based interface allows users to upload a Telugu PDF, select an image preprocessing method, and view the extracted text through a browser-based interface.

---

## 🎯 Project Objectives

- Extract Telugu text from PDF documents.
- Convert PDF pages into processable images.
- Improve OCR quality through image preprocessing.
- Apply Telugu-language Tesseract OCR.
- Provide multiple preprocessing techniques.
- Provide a simple browser-based interface using Gradio.
- Produce editable OCR output for Telugu documents.

---

## ✨ Key Features

### 📄 PDF Document Processing

- Upload Telugu PDF documents.
- Convert PDF pages into images using `pdf2image`.
- Process multiple pages sequentially.

### 🔤 Telugu OCR

- Uses Tesseract OCR.
- Supports Telugu language recognition through the `tel` language model.
- Extracts text page by page.

### 🖼️ Image Preprocessing

The system supports multiple preprocessing approaches:

- Default preprocessing
- Adaptive thresholding
- Edge detection
- Morphological transformation

### 🔬 OpenCV Processing

The preprocessing pipeline uses:

- Grayscale conversion
- Gaussian blur
- Gamma correction
- Otsu thresholding
- Adaptive thresholding
- Canny edge detection
- Morphological closing
- Image resizing

### 🌐 Gradio Interface

The application provides:

- PDF upload
- Preprocessing method selection
- OCR execution
- Extracted Telugu text display

---

## 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| OCR Engine | Tesseract OCR |
| Computer Vision | OpenCV |
| Numerical Computing | NumPy |
| PDF Processing | pdf2image |
| Image Processing | Pillow |
| User Interface | Gradio |
| Development Environment | Google Colab / Python |
| Version Control | Git & GitHub |

---

## 🏗️ System Architecture

```text
                Telugu PDF Document
                         │
                         ▼
                PDF → Image Conversion
                         │
                         ▼
                 Image Preprocessing
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       Default      Adaptive        Morphological
     Processing     Thresholding    Processing
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                   Tesseract OCR
                   Telugu Language
                         │
                         ▼
                 Extracted Telugu Text
                         │
                         ▼
                  Gradio Web Interface
```

---

## 🧠 OCR Processing Pipeline

```text
PDF Upload
    │
    ▼
Read PDF
    │
    ▼
Convert Pages to Images
    │
    ▼
Resize Image
    │
    ▼
Image Preprocessing
    │
    ▼
Telugu Tesseract OCR
    │
    ▼
Extract Text
    │
    ▼
Display Result
```

---

## 🔬 Image Preprocessing Methods

### 1. Default Processing

The default pipeline applies:

```text
Resize
  ↓
Grayscale
  ↓
Gaussian Blur
  ↓
Gamma Correction
  ↓
Otsu Thresholding
  ↓
Morphological Closing
```

### 2. Adaptive Thresholding

Converts the image to grayscale and applies adaptive Gaussian thresholding to separate text from the background.

### 3. Edge Detection

Uses the Canny edge detection algorithm to identify strong edges within the document image.

### 4. Morphological Processing

Uses Otsu thresholding followed by morphological closing to improve the structure of detected text regions.

---

## 🔤 Telugu OCR

The system uses Tesseract OCR with the Telugu language model:

```python
pytesseract.image_to_string(
    image,
    lang="tel"
)
```

The Telugu language data must be installed for Tesseract to recognize Telugu characters.

---

## 🌐 Gradio Application

The application provides a simple interface where users can:

1. Upload a Telugu PDF.
2. Select a preprocessing method.
3. Run OCR.
4. View extracted Telugu text.

---

## 📸 Application Screenshots

### OCR Interface

![OCR Interface](screenshots/interface.png)

### Code Output

![Code Output](screenshots/code_output.png)

### Telugu to English Translation

![Telugu to English Translation](screenshots/telugu_to_english_translator.png)

### PDF Upload

![PDF Upload](screenshots/uploading_the_file.png)

---

## 📁 Repository Structure

```text
Telugu-OCR-Text-Extraction/
│
├── backend/
│   └── app.py
│
├── docs/
│   ├── Introduction-to-OCR-and-Tesseract.pptx
│   ├── OCR_Poster.pdf
│   └── OCR_Report.pdf
│
├── notebooks/
│   └── Untitled13_colab_export.py
│
├── screenshots/
│   ├── code_output.png
│   ├── interface.png
│   ├── telugu_to_english_translator.png
│   └── uploading_the_file.png
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/kandakatlavaruntej/Telugu-OCR-Text-Extraction.git

cd Telugu-OCR-Text-Extraction
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 System Dependencies

Python packages alone are not sufficient for the complete OCR pipeline.

The application also requires:

### Tesseract OCR

Install Tesseract OCR and the Telugu language data.

The application expects Tesseract at:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

If Tesseract is installed elsewhere, update the path in:

```text
backend/app.py
```

### Poppler

`pdf2image` requires Poppler to convert PDF pages into images.

Install Poppler and ensure its executable directory is available to the system.

---

## 🚀 Run the Application

From the repository root:

```bash
python backend/app.py
```

The Gradio interface will provide a local URL.

Open the displayed URL in your browser.

---

## 🧪 Usage

1. Start the application.
2. Open the Gradio interface.
3. Upload a Telugu PDF.
4. Select a preprocessing method.
5. Click **Extract Telugu Text**.
6. Wait for PDF pages to be processed.
7. Review the extracted Telugu text.

---

## 📚 Documentation

Additional project materials are available under:

```text
docs/
```

The documentation includes:

- OCR and Tesseract presentation
- Project poster
- Project report

The original Colab implementation is preserved under:

```text
notebooks/
```

---

## 🔬 Project Workflow

The project follows this workflow:

```text
Input Telugu PDF
       │
       ▼
PDF Page Conversion
       │
       ▼
OpenCV Image Processing
       │
       ▼
Preprocessing Method
       │
       ▼
Tesseract Telugu OCR
       │
       ▼
Extracted Telugu Text
       │
       ▼
Gradio Output
```

---

## 🔮 Future Enhancements

Potential improvements include:

- Telugu-to-English translation integration.
- OCR confidence scoring.
- Automatic preprocessing-method selection.
- OCR result export to TXT, JSON, and DOCX.
- Multi-language OCR support.
- Improved document layout preservation.
- Table and structured-document extraction.
- Batch PDF processing.
- Cloud deployment.
- REST API support.

---

## ⚠️ Limitations

OCR accuracy can vary depending on:

- Scan quality
- Image resolution
- Font style
- Document layout
- Noise and background artifacts
- Telugu language model quality
- Preprocessing method

The current preprocessing selection is based on the method selected by the user rather than an OCR-confidence-based automatic selection mechanism.

---

## 👨‍💻 Author

**Kandakatla Varun Tej**

GitHub:  
https://github.com/kandakatlavaruntej

LinkedIn:  
https://www.linkedin.com/in/kandakatla-varun-tej-a7a96b12b

---

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.
