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
    apply OCR on the uploaded image and return the text result. 
    """
    text = pytesseract.image_to_string(Image.open(filename), lang = 'eng')  
    return text



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/upload_medical_documents', methods=('POST', 'GET'))
def upload_medical_documents():
    if request.method == 'POST':
        # check if the uploaded file is supported there is a file in the request
        if 'medical_file' not in request.files:
            print("file not supported")
            return render_template('ocr/upload_medical_documents.html', msg='Invalid file format')

        file = request.files['medical_file']
        # if no file is selected
        if file.filename == '':
            print('file name blank')
            return render_template('ocr/upload_medical_documents.html', msg='No file selected')


        if file and allowed_file(file.filename):

            # call the OCR function on it
            extracted_text = ocr_core(file)
            print(extracted_text)

            # extract the text and display it
            return render_template('ocr/upload_medical_documents.html', ocr_result=extracted_text)


    elif request.method == 'GET':
        return render_template('ocr/upload_medical_documents.html')
