# Make collage
from PIL import Image
import numpy as np

def make_collage(img1, img2, name):
    i1 = np.array(Image.open(img1))
    i2 = np.array(Image.open(img2))

    stacked_image= np.vstack([i1, i2])
    collage = Image.fromarray(stacked_image)
    collage.save(name)

make_collage("./files/image1.jpg", "./files/image2.jpg", "./files/collage.jpg")
