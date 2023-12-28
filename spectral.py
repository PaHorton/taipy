import astropy.units as u
from astropy.utils import data
from spectral_cube import SpectralCube
from taipy.gui import Gui
import io
import numpy as np
from PIL import Image

fn = data.get_pkg_data_filename('tests/data/example_cube.fits', 'spectral_cube')
cube = SpectralCube.read(fn)
cube = cube/cube.max() * 256

img = Image.fromarray(np.uint8(cube[:,:,0]))
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format='jpeg')
img_byte_arr = img_byte_arr.getvalue()

data = {
    "Frames": range(cube.shape[2]),
    "Average": [cube[:,:,i].mean().to_value() for i in range(cube.shape[2])],
    "Max": [cube[:,:,i].max().to_value() for i in range(cube.shape[2])],
    "Min": [cube[:,:,i].min().to_value() for i in range(cube.shape[2])]
}
page = """
#Spectral Cube Analysis Tool
<|{content}|file_selector|label=Select File|on_action=function_name|extensions=.csv,.xlsx|drop_message=Drop Message|>
<|{img_byte_arr}|image|height=250px|>
<|{data}|chart|mode=lines|x=Frames|y[1]=Average|y[2]=Max|y[3]=Min|line[1]=dash|color[2]=blue|color[3]=red|>
"""


Gui(page).run(use_reloader=True, port=5001)
