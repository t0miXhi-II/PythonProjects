import os
import qrcode

def get_input():
    user_input = input('Enter your url: ')
    return user_input

user_input = get_input()

qr_image = qrcode.make(user_input)

qr_image.save("qr_image.png", "PNG") 

# OLD VERSION #
#import pyqrcode
#qrCode = pyqrcode.create(user_input)
#qrCode.svg('myQRcode.svg', scale=8)
 
