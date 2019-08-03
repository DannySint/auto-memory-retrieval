import os
import io
import requests
from dotenv import load_dotenv

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

load_dotenv()
TESSERACT = os.getenv("TESSERACT")

pytesseract.pytesseract.tesseract_cmd = TESSERACT

def transcribe_image_from_path(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)
    
def transcribe_image_from_url(image_url):
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))
    return pytesseract.image_to_string(image)