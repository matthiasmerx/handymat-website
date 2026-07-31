#!/usr/bin/env python3
"""
compress-images.py

Verkleint en comprimeert foto's voor gebruik op de website, zodat een
enkele portfolio-foto niet meer 2-3 MB weegt. Werkt op JPEG en PNG,
behoudt de bestandsextensie, overschrijft het origineel.

Gebruik:
    python3 compress-images.py images/foto1.jpg images/foto2.png
    python3 compress-images.py images/*.jpg

Vereist: pip install pillow --break-system-packages (waarschijnlijk al
aanwezig als je fix-orientation.py ook gebruikt).

Wat het doet:
- Schaalt af naar maximaal 1600px breed (ruim voldoende voor een
  portfolio-foto op het web, ook op een groot scherm)
- Slaat op met kwaliteit 82 (JPEG) — nauwelijks zichtbaar verschil,
  aanzienlijk kleiner bestand
- Laat de EXIF-orientatie eerst correct verwerken (zoals
  fix-orientation.py), zodat een foto niet alsnog scheef wordt na
  compressie
- Rapporteert de bestandsgrootte voor en na
"""
import sys
import os
from PIL import Image, ImageOps

MAX_WIDTH = 1600
JPEG_QUALITY = 82
PNG_COMPRESS_LEVEL = 9

def human(n):
    for unit in ["B", "KB", "MB"]:
        if n < 1024:
            return f"{n:.0f}{unit}"
        n /= 1024
    return f"{n:.1f}GB"

def compress(path):
    before = os.path.getsize(path)
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)  # rotatie eerst goedzetten

    if img.width > MAX_WIDTH:
        ratio = MAX_WIDTH / img.width
        new_size = (MAX_WIDTH, int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)

    ext = os.path.splitext(path)[1].lower()
    if ext in (".jpg", ".jpeg"):
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(path, "JPEG", quality=JPEG_QUALITY, optimize=True)
    elif ext == ".png":
        img.save(path, "PNG", optimize=True, compress_level=PNG_COMPRESS_LEVEL)
    else:
        print(f"Overgeslagen (onbekend formaat): {path}")
        return

    after = os.path.getsize(path)
    saved_pct = (1 - after / before) * 100 if before else 0
    print(f"{path}: {human(before)} -> {human(after)}  ({saved_pct:.0f}% kleiner)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Geef minstens 1 bestandspad mee.")
        sys.exit(1)
    for p in sys.argv[1:]:
        try:
            compress(p)
        except Exception as e:
            print(f"Mislukt voor {p}: {e}")
