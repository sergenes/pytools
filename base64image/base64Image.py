from io import BytesIO

import base64
from PIL import Image
import os


def image_to_base64_html_string(png_image_name):
    """
    Convert PNG image file to a base64 encoded string for HTML img tag.

    :param png_image_name: Name of the PNG image file in the same folder.
    :return: Base64 encoded string suitable for HTML img tag.
    """
    # Ensure the file exists and has the right extension
    if not os.path.exists(png_image_name) or not png_image_name.lower().endswith('.png'):
        raise ValueError("The provided file either doesn't exist or is not a PNG image.")

    with Image.open(png_image_name) as image:
        # Ensure it's a PNG
        if image.format != 'PNG':
            raise ValueError("The provided file is not a PNG image.")

        # Convert to bytes
        buffered = BytesIO()
        image.save(buffered, format="PNG")

        # Encode bytes to base64 string
        img_str = base64.b64encode(buffered.getvalue()).decode()

        # Format the string for HTML img tag
        html_string = f"data:image/png;base64,{img_str}"

        return html_string


# /usr/local/bin/python3.11 base64Image.py
if __name__ == '__main__':
    img_string = image_to_base64_html_string("undo_white.png")
    html_tag = f'<img src="{img_string}" alt="Base64 encoded image" />'
    print(html_tag)


