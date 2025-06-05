import qrcode
def read_text_file(file_path):
  with open(file_path,"r")as file:
    text=file.read()
  return text
file_path="msg.txt"
text="read_text_file
r=qrcode.QRCode()
r.add_data(text_message)
r.make(fit=True)
img=r.make_image(fill_color="Black",back_color="white")
img.save("path")
