# -Scropy

Dieses Skript verwendet Tesseract OCR, um Text aus dem neuesten Screenshot in einem angegebenen Verzeichnis zu extrahieren und in die Zwischenablage zu kopieren.

## Voraussetzungen

- Python 3.x
- Tesseract OCR (Installationspfad anpassen)
- Python-Bibliotheken: `pytesseract`, `pyperclip`, `Pillow`

## Installation

1. Installiere Tesseract OCR und stelle sicher, dass der Pfad korrekt ist:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
