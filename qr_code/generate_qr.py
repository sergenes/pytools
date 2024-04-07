import qrcode
from PIL import Image


def generate_qr_code_with_image(data, output_filename, logo_path):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="red", back_color="white").convert('RGBA')
    img = img.resize((512, 512), Image.Resampling.LANCZOS)

    # Add main logo to the center of the QR code
    logo = Image.open(logo_path)
    logo = logo.resize((64, 64), Image.Resampling.LANCZOS)
    logo_pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)

    img.paste(logo, logo_pos, mask=logo)
    img.save(output_filename)


# /usr/local/bin/python3.11 generate_qr-.py
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
