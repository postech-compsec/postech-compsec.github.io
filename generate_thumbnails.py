# usage: python3 generate_thumbnails.py
# to re-generate thumbnails for all images, comment out :24-25

import os
from pathlib import Path
from PIL import Image, ImageOps

# --- configurations ---
SOURCE_DIR = Path("assets/gallery")
THUMB_DIR = Path("assets/gallery/thumbnails")
THUMB_SIZE = (800, 800)
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png']
# ------------

def generate_thumbnails():
    
    THUMB_DIR.mkdir(parents=True, exist_ok=True)
        
    for file_path in SOURCE_DIR.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in IMAGE_EXTENSIONS:
            thumb_path = THUMB_DIR / file_path.with_suffix('.webp').name

            # to re-generate thumbnails for all images, comment out HERE #
            if thumb_path.exists():
                continue
            ##############################################################

            try:
                print(f"  > Creating: {thumb_path.name}")
                with Image.open(file_path) as img:
                    img = ImageOps.exif_transpose(img)
                    if img.mode in ('RGBA', 'LA'):
                        img = img.convert('RGBA')
                    else:
                        img = img.convert('RGB')
                    thumb = ImageOps.fit(img, THUMB_SIZE, Image.Resampling.LANCZOS)                    
                    thumb.save(thumb_path, format='WEBP', quality=100)
            except Exception as e:
                print(f"Could not process {file_path.name}: {e}")

    print("Thumbnail generation complete.")

if __name__ == "__main__":
    generate_thumbnails()