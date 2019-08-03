import os
from dotenv import load_dotenv

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

load_dotenv()
TESSERACT = os.getenv("TESSERACT")

pytesseract.pytesseract.tesseract_cmd = TESSERACT

print(pytesseract.image_to_string(Image.open('data/cucumber.png')))