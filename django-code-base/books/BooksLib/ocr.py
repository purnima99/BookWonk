import cv2
import numpy as np
import requests
import io
import json
import os

class OCR :
    def __init__(self):
        self.url_api = "https://api.ocr.space/parse/image"
    
    def ocr (self, img) :
        _, compressedimage = cv2.imencode(".jpg", img, [1, 90])
        file_bytes = io.BytesIO(compressedimage)
        result = requests.post(self.url_api,
              files = {"ocr.jpeg": file_bytes},
              data = {"apikey": "helloworld",
                      "language": "eng"})
        result = result.content.decode()
        result = json.loads(result)

        parsed_results = result.get("ParsedResults")[0]
        text_detected = parsed_results.get("ParsedText")

        return  text_detected