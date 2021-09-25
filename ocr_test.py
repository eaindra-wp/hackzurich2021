import pytesseract
from PIL import Image


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # pytesseract.pytesseract.tesseract_cmd = r'/home/eaindra/hackzurich2021/hackzurich2021/lib/python3.8/site-packages/pytesseract/'
    text = pytesseract.image_to_string(Image.open(filename), lang = 'eng')  
    # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


print(ocr_core(r'/home/eaindra/hackzurich2021/checkout_data.jpg'))