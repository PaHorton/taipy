from taipy.gui import Gui
from PIL import Image
import random
import glob
import csv

image_paths = glob.glob("images/*")

def get_image(paths):
    n = random.randrange(0,len(paths))
    return paths[n]

def bowl_pressed(state):
    with open('bowl_plate.csv','a',newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow([state.image_path, "Bowl"])
    path = get_image(image_paths)
    state.image_path = path

def plate_pressed(state):
    with open('bowl_plate.csv','a',newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow([state.image_path, "Plate"])
    path = get_image(image_paths)
    state.image_path = path

image_path = get_image(image_paths)

page = """
#Bowls or Plates
<|{image_path}|image|height=250px|>

<|Bowl|button|on_action=bowl_pressed|>
<|Plate|button|on_action=plate_pressed|>
"""

Gui(page).run(use_reloader=True, port=5001)
