import pyqrcode

genQR = pyqrcode.create("This is a message embed in QR-code")
genQR.png('newQR.png',scale=5)

#from pdf2jpg import pdf2jpg
#result = pdf2jpg.convert_pdf2jpg("pdfQR.pdf","QRfolder",pages="1")

from pyzbar.pyzbar import decode
from PIL import Image
result = decode(Image.open("newQR.png"))
print(str(result[0].data)[2:-1])
