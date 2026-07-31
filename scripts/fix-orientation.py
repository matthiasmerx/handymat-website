#!/usr/bin/env python3
"""
fix-orientation.py

Corrigeert de rotatie van foto's definitief: leest het EXIF-orientatie-
vlaggetje van de telefoon en draait de daadwerkelijke pixels, zodat de
foto er in elke tool (browser, AI-tool, editor) rechtop uitziet, ook als
die tool het EXIF-vlaggetje zelf negeert.

Gebruik:
    python3 fix-orientation.py pad/naar/foto1.jpg pad/naar/foto2.jpg
    python3 fix-orientation.py images/*.jpg

Vereist: pip install pillow --break-system-packages
"""
import sys
from PIL import Image, ImageOps

def fix(path):
    img = Image.open(path)
    fixed = ImageOps.exif_transpose(img)  # past pixels aan volgens EXIF-tag
    fixed.save(path)  # overschrijft, zonder EXIF-orientatie-afhankelijkheid meer
    print(f"Gecorrigeerd: {path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Geef minstens 1 bestandspad mee.")
        sys.exit(1)
    for p in sys.argv[1:]:
        try:
            fix(p)
        except Exception as e:
            print(f"Mislukt voor {p}: {e}")
