import pytesseract
import pyperclip
from PIL import Image
import os

# Pfad zu Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Pfad zum Screenshot-Verzeichnis
screenshot_dir = r'C:\Users\eyama\Pictures\Screenshots'

# Screenshot-Datei
list_of_files = [os.path.join(screenshot_dir, f) for f in os.listdir(screenshot_dir)
                 if os.path.isfile(os.path.join(screenshot_dir, f))]
latest_file = max(list_of_files, key=os.path.getctime)

# Screenshot öffnen
screenshot = Image.open(latest_file)

# OCR verwenden
extracted_text = pytesseract.image_to_string(screenshot)

# in Zwischenablage kopieren
pyperclip.copy(extracted_text)

# Enxtrahierte Text ausgeben
print(extracted_text)
