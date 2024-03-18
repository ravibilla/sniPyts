# Generate QR code
#!pip install PyQRCode
#!pip install pypng
import pyqrcode
import png

link = "https://www.instagram.com/ravibilla/"
qr_code = pyqrcode.create(link)
qr_code.png("./files/instagram.png", scale=5)