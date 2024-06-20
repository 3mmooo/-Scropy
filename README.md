# Scropy
 
# OCR-Screenshot-Extractor

Ein Python-Skript, das den neuesten Screenshot aus einem angegebenen Verzeichnis liest, Text daraus extrahiert und den Text in die Zwischenablage kopiert. Das Skript verwendet Tesseract OCR für die Texterkennung und Pyperclip für die Zwischenablagefunktionalität.

## Voraussetzungen

Stelle sicher, dass die folgenden Abhängigkeiten installiert sind:

- [Python](https://www.python.org/downloads/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Python-Bibliotheken:
  - pytesseract
  - pyperclip
  - Pillow

Du kannst die Python-Bibliotheken mit folgendem Befehl installieren:

```bash
pip install pytesseract pyperclip Pillow
```

## Installation

1. Installiere [Tesseract OCR](https://github.com/tesseract-ocr/tesseract). Folge den Anweisungen auf der GitHub-Seite, um es auf deinem System zu installieren.
2. Klone dieses Repository oder lade die ZIP-Datei herunter und entpacke sie.

## Verwendung

1. Stelle sicher, dass du den Pfad zu Tesseract OCR in der Python-Datei richtig konfiguriert hast:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

2. Setze den Pfad zu deinem Screenshot-Verzeichnis:

```python
screenshot_dir = r'C:\Users\User\Pictures\Screenshots'
```

3. Führe das Skript aus:

```bash
python ocr_screenshot_extractor.py
```

Das Skript findet den neuesten Screenshot im angegebenen Verzeichnis, extrahiert den Text daraus und kopiert den extrahierten Text in die Zwischenablage.

## Beispiel

Nach dem Ausführen des Skripts wird der extrahierte Text auf der Konsole ausgegeben und in die Zwischenablage kopiert, sodass du ihn einfach in ein Dokument oder ein Textfeld einfügen kannst.


