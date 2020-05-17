# users/picture_handler.py

# Python Imaging Library (PIL)
# The Python Imaging Library (PIL) adds image processing capabilities
# to your Python interpreter. This library supports many file formats,
# and provides powerful image processing and graphics capabilities.

import os
from PIL import Image
from flask import url_for, current_app

def add_profile_pic(pic_upload, username):
    """
    The function accepts uploaded file and username.
    1) Takes name of the uploaded image file
    2) Extracts its extension.
    3) Create new name for the file
    4) Create path where the file will be saved in static directory
    5) Point out standart image SIZE
    6) Open uploaded file through instant of class Image
    7) Set size of the image
    8) Save uploaded image file in correct directory with correct name
    9) Return name of the file.

    """

    filename = pic_upload.filename       # ??????
    ext_type = filename.split('.')[-1]
    storage_filename = str(username) + '.' + ext_type

    filepath = os.path.join(current_app.root_path, 'static/profile_pics', storage_filename)

    output_size = (200, 200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
