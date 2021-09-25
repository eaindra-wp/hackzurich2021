import pytesseract
from PIL import Image
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('ocr', __name__, url_prefix='/ocr')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = '/static/uploads/'

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # pytesseract.pytesseract.tesseract_cmd = r'/home/eaindra/hackzurich2021/hackzurich2021/lib/python3.8/site-packages/pytesseract/'
    text = pytesseract.image_to_string(Image.open(filename), lang = 'eng')  
    # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/upload_medical_documents', methods=('POST', 'GET'))
def upload_medical_documents():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'document-one' not in request.files:
            print("file not  supported")
            return render_template('ocr/upload_medical_documents.html', msg='No file selected')

        file = request.files['document-one']
        # if no file is selected
        if file.filename == '':
            print('file name blank')
            return render_template('ocr/upload_medical_documents.html', msg='No file selected')


        if file and allowed_file(file.filename):

            # call the OCR function on it
            extracted_text = ocr_core(file)
            print(extracted_text)

            # extract the text and display it
            return render_template('ocr/upload_medical_documents.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename,
                                   logged_in_username=session['user_id'] )
                                   
    elif request.method == 'GET':
        return render_template('ocr/upload_medical_documents.html')
