import pyqrcode

genQR = pyqrcode.create("This is a message embed in QR-code") #CREATE QRCODE
genQR.png('newQR.png',scale=5) #CREARE PNG

##CONVERT PDF TO JPG
#from pdf2jpg import pdf2jpg
#result = pdf2jpg.convert_pdf2jpg("pdfQR.pdf","QRfolder",pages="1")

from pyzbar.pyzbar import decode #TO DECODE
from PIL import Image #TO READ IMG

## FOR PDF
#result = decode(Image.open("QRfolder//allQR.pdf//1_allQR.pdf.jpg",'r'))

#READ QRCODE
result = decode(Image.open("newQR.png"))
#list = str(result[0].data).replace("\\r","").replace("\\n\\n","")[2:-1].split("\\n") #REMOVE UNNECESSARY PART(FOR NWCOM)
print(str(result[0].data)[2:-1]) #PRINT `resukt`
