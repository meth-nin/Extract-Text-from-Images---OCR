from PIL import Image, ImageEnhance

def preprocess_image(image_path):
    img = Image.open(image_path)

    # Convert to grayscale
    gray = img.convert("L")

    # Resize (improves OCR accuracy)
    w, h = gray.size
    gray = gray.resize((w * 2, h * 2), Image.LANCZOS)

    # Increase contrast
    gray = ImageEnhance.Contrast(gray).enhance(2.0)

    # Binarization
    bw = gray.point(lambda x: 0 if x < 140 else 255, "1")

    return bw