import qrcode
text="hello"
r=qrcode.QRCode()
r.add_data(text)
r.make(fit=True)
img=r.make_image{fill_color="Black",back_color="white"
img.save("path")
