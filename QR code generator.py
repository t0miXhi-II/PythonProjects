import pyqrcode

def get_input():
    user_input = input('Enter your url: ')
    return user_input

user_input = get_input()
qrCode = pyqrcode.create(user_input)
qrCode.svg('myQRcode.svg', scale=8)

