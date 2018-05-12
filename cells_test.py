import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
im = Image.open("map1.jpeg")
gray = im.convert("L")
gray.show()
values = gray.split()
print(values)