# Decode qr code
# brew install zbar # On Mac OSX
#!pip install pyzbar
#!pip install pillow
from pyzbar.pyzbar import decode
from PIL import Image

decoded_qr = decode(Image.open("./files/instagram.png"))
print(decoded_qr[0].data.decode('ascii'))