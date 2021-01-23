import qrcode
import qrcode.image.svg

# basic qr code making
qr_img = qrcode.make("This is my first QR code")
qr_img.save("QR1.jpg")

# Custom QR code
qr_img = qrcode.QRCode(version=2,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size = 60,
                        border = 2)

qr_img.add_data("https://github.com/omsatam")
qr_img.make(fit=True)
qr_image = qr_img.make_image(fill_color = "purple", back_color = "white")
qr_image.save("QR2.jpg")

# For making a QR code in SVG format
factory = qrcode.image.svg.SvgPathImage
svg_image = qrcode.make("This is QR code in a SVG format", image_factory = factory)
svg_image.save("QR3.svg")