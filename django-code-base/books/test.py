from BooksLib import ocr
import cv2

img = cv2.imread("ocrtest.jpeg")
ocrObj = ocr.OCR()

text = ocrObj.ocr(img)
print(text)