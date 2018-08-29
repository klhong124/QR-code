import pyqrcode

genQR = pyqrcode.create("This is a message embed in QR-code")
genQR.png('newQR.png',scale=5)

#from pdf2jpg import pdf2jpg
#result = pdf2jpg.convert_pdf2jpg("pdfQR.pdf","QRfolder",pages="1")

from pyzbar.pyzbar import decode
from PIL import Image
#result = decode(Image.open("QRfolder//allQR.pdf//1_allQR.pdf.jpg",'r'))
result = decode(Image.open("TEST.jpg"))
list = str(result[0].data).replace("\\r","").replace("\\n\\n","")[2:-1].split("\\n")
print(list)
