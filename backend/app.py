import os
import cv2
import numpy as np
import gradio as gr
import pytesseract
from pdf2image import convert_from_path


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

# Windows users may need to change this path depending
# on where Tesseract OCR is installed.
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if os.path.exists(TESSERACT_PATH):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


# ---------------------------------------------------------
# Image Preprocessing Functions
# ---------------------------------------------------------

def rescale_frame(frame, scale=0.75):
    """Resize an image while maintaining its dimensions ratio."""
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv2.resize(
        frame,
        dimensions,
        interpolation=cv2.INTER_AREA
    )


def apply_gamma(image, gamma=1.0):
    """Apply gamma correction to improve image visibility."""
    inv_gamma = 1.0 / gamma

    table = np.array([
        ((i / 255.0) ** inv_gamma) * 255
        for i in np.arange(0, 256)
    ]).astype("uint8")

    return cv2.LUT(image, table)


def adaptive_threshold(image):
    """Apply adaptive thresholding."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )


def edge_detection(image):
    """Detect edges using the Canny algorithm."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return cv2.Canny(gray, 50, 150)


def morphological_transformation(image):
    """Apply morphological closing to the image."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (3, 3)
    )

    return cv2.morphologyEx(
        binary,
        cv2.MORPH_CLOSE,
        kernel
    )


def process_image(image, method="default"):
    """Apply the selected preprocessing method."""

    resized_image = rescale_frame(image)

    if method == "default":
        gray = cv2.cvtColor(
            resized_image,
            cv2.COLOR_BGR2GRAY
        )

        blur = cv2.GaussianBlur(
            gray,
            (3, 3),
            0
        )

        gamma_corrected = apply_gamma(
            blur,
            gamma=0.3
        )

        _, thresholded = cv2.threshold(
            gamma_corrected,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (3, 3)
        )

        return cv2.morphologyEx(
            thresholded,
            cv2.MORPH_CLOSE,
            kernel
        )

    elif method == "adaptive_threshold":
        return adaptive_threshold(resized_image)

    elif method == "edge_detection":
        return edge_detection(resized_image)

    elif method == "morphological":
        return morphological_transformation(resized_image)

    return resized_image


# ---------------------------------------------------------
# OCR
# ---------------------------------------------------------

def extract_text_from_image(image, language="tel"):
    """Extract Telugu text using Tesseract OCR."""

    return pytesseract.image_to_string(
        image,
        lang=language
    )


# ---------------------------------------------------------
# PDF Processing
# ---------------------------------------------------------

METHODS = [
    "default",
    "adaptive_threshold",
    "edge_detection",
    "morphological"
]


def process_pdf(pdf_path, selected_method="default"):
    """
    Convert PDF pages to images, preprocess each page,
    and extract Telugu text using Tesseract OCR.
    """

    if pdf_path is None:
        return "Please upload a PDF file."

    try:
        pages = convert_from_path(pdf_path)

    except Exception as error:
        return (
            "Unable to convert the PDF into images.\n\n"
            f"Error: {error}"
        )

    extracted_texts = []

    for page_number, page in enumerate(pages, start=1):

        page_image = np.array(page)

        # PIL image is RGB.
        # OpenCV processing expects BGR.
        page_image = cv2.cvtColor(
            page_image,
            cv2.COLOR_RGB2BGR
        )

        processed_image = process_image(
            page_image,
            method=selected_method
        )

        text = extract_text_from_image(
            processed_image,
            language="tel"
        )

        extracted_texts.append(
            f"Page {page_number}\n{text}"
        )

    return "\n\n".join(extracted_texts)


# ---------------------------------------------------------
# Gradio Interface
# ---------------------------------------------------------

with gr.Blocks(
    title="Telugu OCR Text Extraction"
) as interface:

    gr.Markdown(
        """
        # తెలుగు OCR Text Extraction

        Upload a Telugu PDF document and extract
        its text using Tesseract OCR.

        The system converts PDF pages into images,
        applies OpenCV preprocessing, and performs
        Telugu-language OCR.
        """
    )

    pdf_input = gr.File(
        label="Upload Telugu PDF",
        file_types=[".pdf"],
        type="filepath"
    )

    preprocessing_method = gr.Dropdown(
        choices=METHODS,
        value="default",
        label="Preprocessing Method"
    )

    extract_button = gr.Button(
        "Extract Telugu Text"
    )

    output_text = gr.Textbox(
        label="Extracted Telugu Text",
        lines=20
    )

    extract_button.click(
        fn=process_pdf,
        inputs=[
            pdf_input,
            preprocessing_method
        ],
        outputs=output_text
    )


# ---------------------------------------------------------
# Application Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    interface.launch()