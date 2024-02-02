# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
# pip install Pillow

from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / '20180310_122007.JPG'
NEW_IMAGE = ROOT_FOLDER / 'NEW 20180310_122007.JPG'

pil_image = Image.open(ORIGINAL)
# print(pil_image.size)
width, height = pil_image.size
exif = pil_image.info['exif']  # info da foto, nao usar para diminuir o tamanho

# regra de 3
# width ---- new width
# height --- x

new_width = 1000
new_height = round(new_width * height / width)
print(new_width, new_height)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    exif=exif,
)
