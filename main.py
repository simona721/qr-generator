import qrcode

qrCreator = str(input("Enter a website for a qr code: "))

img = qrcode.make(qrCreator)
print(img)
img.save(f"{qrCreator}.png")


