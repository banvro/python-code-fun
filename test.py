from rembg import remove
from PIL import Image

img = Image.open("man.jpg")
out = remove(img)
out.save("no_bg.png")
