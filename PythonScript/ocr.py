import pytesseract
pytesseract.pytesseract.tesseract_cmd = r''
print(pytesseract.image_to_string(r'ok.png'))
