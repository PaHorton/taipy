from taipy.gui import Gui
import random
import glob
import csv
import numpy as np
import io
from PIL import Image

image_paths = glob.glob("mcam/test_novel/all/*.npy")

def get_image(paths):
    n = random.randrange(0,len(paths))
    data = np.load(paths[n])
    img = Image.fromarray(np.uint8(data[:,:,(2,0,1)]))
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return paths[n], img_byte_arr

def strange_pressed(state):
    with open('mastcam.csv','a',newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow([state.path, "Strange"])
    path, image = get_image(image_paths)
    state.image = image
    state.path = path

def not_strange_pressed(state):
    with open('mastcam.csv','a',newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow([state.path, "Normal"])
    path, image = get_image(image_paths)
    state.image = image
    state.path = path

path, image = get_image(image_paths)

page = """
#Mastcam Image Analysis
<|{image}|label={path}|image|height=250px|>

<|Strange|button|on_action=strange_pressed|>
<|Not Strange|button|on_action=not_strange_pressed|>
"""

Gui(page).run(use_reloader=True, port=5001)
