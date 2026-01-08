import pytesseract
from preprocess import preprocess_image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\Methupa-Thyaga\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

def extract_text(image_path):
    processed_image = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_image)
    return text.replace("\x0c", "").strip()