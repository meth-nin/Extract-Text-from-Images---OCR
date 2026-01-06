import pytesseract
from preprocess import preprocess_image

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Methupa-Thyaga\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

image_path = "23a93669523149a78a1d20153fc74610.jpg"

processed_image = preprocess_image(image_path)

text = pytesseract.image_to_string(processed_image)

clean_text = text.replace("\x0c", "").strip()
print(clean_text)