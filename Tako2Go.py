import qrcode
from PIL import Image 

def generate_blue_on_white_qr_code_with_logo(data, logo_path, filename="blue_on_white_qr.png"): 
    """
    Generates a QR code with blue modules and a white background,
    with a logo image embedded in the center.

    Args:
        data (str): The data (e.g., a link) to encode in the QR code.
        logo_path (str): The file path to the logo image.
        filename (str): The name of the output image file.
    """
    qr = qrcode.QRCode(
        version=None, 
        error_correction=qrcode.constants.ERROR_CORRECT_H, 
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB") 

    
    try:
        logo = Image.open(logo_path)
    except FileNotFoundError:
        print(f"Error: Logo image not found at {logo_path}. QR code generated without logo.")
        img.save(filename)
        return

    qr_width, qr_height = img.size
    logo_max_size = qr_width // 3.5 

    logo.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS) 

    x = (qr_width - logo.width) // 2
    y = (qr_height - logo.height) // 2

    img.paste(logo, (x, y), logo if logo.mode == 'RGBA' else None) 
   

    img.save(filename)

my_link = "http://tako2go.menus.run/"
my_logo = "Tako2Go_Logo.jpg" 

generate_blue_on_white_qr_code_with_logo(my_link, my_logo, "Tako2Goqr_with_logo.png") 

print("QR code with logo generated!")