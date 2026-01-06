from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Methupa-Thyaga\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

image = Image.open("23a93669523149a78a1d20153fc74610.jpg")

gray_image = image.convert("L")

text = pytesseract.image_to_string(gray_image)

clean_text = text.replace("\x0c", "").strip()
print(clean_text)