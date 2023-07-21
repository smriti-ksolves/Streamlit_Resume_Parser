import pytesseract
from pdf2image import convert_from_path
import os
import cv2
from dotenv import load_dotenv

load_dotenv()
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


def file_extract(file_path, file_type, destination_path='pdfs/extracted.txt'):
    if file_type == "application/pdf":

        images = convert_from_path(file_path,
                                   poppler_path=os.getenv("POPPLER_PATH"))
        for i in range(len(images)):
            images[i].save('page' + str(i) + '.jpg', 'JPEG')
            img = 'page' + str(i) + '.jpg'
            text = str(pytesseract.image_to_string(img))
            with open(f'{destination_path}', 'a') as f:
                f.write(text)
            os.remove(img)
    else:
        img = cv2.imread(file_path)
        text = str(pytesseract.image_to_string(file_path))
        with open(f'{destination_path}', 'a') as f:
            f.write(text)

# pdf_extract("pdfs\SMRITI_RESUME.pdf")
