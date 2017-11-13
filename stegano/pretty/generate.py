from PIL import Image
from random import randint as rnd

flag = Image.open("flag.png")
fpix = flag.load()
img1 = Image.open("pretty.png")
pix1 = img1.load()

for i in range(667):
  for j in range(1000):
    r, g, b = fpix[j, i]
    r1, g1, b1 = pix1[j, i]
    
    # check for not-white :)
    if r < 200 or g < 200 or b < 200:
        # reverse two lower bits for better visibility
        r1 = r1 ^ 3
        g1 = g1 ^ 3
        b1 = b1 ^ 3
    
    pix1[j, i] = r1, g1, b1

img1.save("very-pretty.png", compress_level=0)