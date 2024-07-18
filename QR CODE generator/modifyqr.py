import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction= qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)

                 
qr.add_data("https://youtu.be/HY-TBa_Y2-M?si=U8YZk99tYMkM8Agh")                 
qr.make(fit=True)
# modify it
img=qr.make_image(fill_color="black",back_color="white")

img.save("2ndqr.png")



 