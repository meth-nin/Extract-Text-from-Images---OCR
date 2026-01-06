from PIL import Image, ImageEnhance

def preprocess_image(image_path):
    img = Image.open(image_path)

    # grayscale
    gray_img = img.convert("L")

    # resize
    width, height = gray_img.size
    gray_img = gray_img.resize((width * 2, height * 2), Image.LANCZOS)

    # increase contrast
    gray_img = ImageEnhance.Contrast(gray_img).enhance(2.0)

    # binarization
    bw = gray_img.point(lambda x: 0 if x < 140 else 255, '1')

    return bw