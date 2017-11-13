from PIL import Image
from random import randint as rnd

image = Image.open("uctf_task_source.png")
ipix  = image.load()
flag  = Image.open("uctf_task_flag.png")
fpix  = flag.load()
wrong = Image.open("uctf_task_wrong.png")
wpix  = wrong.load()

res   = Image.new("RGB", (400, 400))
rpix  = res.load()

for i in range(400):
    for j in range(400):
        # original is RGBA image
        r, g, b, a = ipix[j, i]
               
        # flag and wrong are black&white images
        fc = fpix[j, i]
        wc = wpix[j, i]
        
        # flag in green 0 layer
        # check for white
        if fc > 127:
            g = g | 1
        else:
            g = g & 254
        
        # wrong in red, blue 0 layer
        # check for white
        if wc > 127:
            r = r | 1
            b = b | 1
        else:
            r = r & 254
            b = b & 254
        
        rpix[j, i] = r, g, b

res.save("best-logotype.png", compress_level=0)
