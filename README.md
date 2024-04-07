# Python App Development Tools

This project provides a set of tools useful for app development written in Python. It currently includes two tools:

1. QR Code Generator for App Store Links
2. PNG to Base64 Converter for HTML img Tags

## QR Code Generator

The QR Code Generator creates QR codes that link to apps on the Apple App Store and Google Play Store. It includes embedded Apple and Google logos in the center of the QR codes.

### Usage

```python
if __name__ == '__main__':
    # Define the input string and the file names
    app_name = "voice_bridge"
    input_string_apple = "https://apps.apple.com/us/app/speech-translator-be-heard/id6479205508"
    input_string_google = "https://play.google.com/store/apps/details?id=com.answersolutions.talkwise.voicebridge"
    output_filename_apple = "apple_" + app_name + "_qr_code.png"
    output_filename_google = "google_" + app_name + "_qr_code.png"
    logo_path_apple = "stores_apple.png"
    logo_path_google = "stores_play.png"

    generate_qr_code_with_image(input_string_apple, output_filename_apple, logo_path_apple)
    generate_qr_code_with_image(input_string_google, output_filename_google, logo_path_google)
```

### Result

<table>
  <tr>
    <td>Apple Store Link</td>
     <td>Google Play Link</td>
  </tr>
  <tr>
    <td><img src="./qr_code/apple_upwrite_qr_code.png" width=256></td>
    <td><img src="./qr_code/google_upwrite_qr_code.png" width=256></td>
  </tr>
 </table>

## PNG to Base64 Converter

The PNG to Base64 Converter tool converts PNG image files to base64-encoded strings for use in HTML <img> tags. It can be useful when developing Chrome or Safari extensions or in other cases where you cannot deploy PNG images with your code.

### Usage

```python
# /usr/local/bin/python3.11 base64Image.py
if __name__ == '__main__':
    img_string = image_to_base64_html_string("undo_white.png")
    html_tag = f'<img src="{img_string}" alt="Base64 encoded image" />'
    print(html_tag)
```

## Dependencies

- Python 3.11
- `from io import BytesIO`
- `base64`
- `PIL` (Python Imaging Library)

### Installation

You can install the required dependencies using pip. Run the following command in your terminal:

```bash
pip install pillow
```

