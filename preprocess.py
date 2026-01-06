from PIL import Image, ImageEnhance
import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Methupa-Thyaga\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

img = Image.open("23a93669523149a78a1d20153fc74610.jpg")

#gray scale
gray_img = img.convert("L")

#resize
width, height = gray_img.size
gray_img_re = gray_img.resize((width*2, height*2), Image.LANCZOS)

#contrast
gray_img_re = ImageEnhance.Contrast(gray_img_re).enhance(2.0)

#binarization
bw = gray_img_re.point(lambda x: 0 if x < 140 else 255, '1')

#ocr
text = pytesseract.image_to_string(bw)

clean_text = text.replace("\x0c", "").strip()
print(clean_text)