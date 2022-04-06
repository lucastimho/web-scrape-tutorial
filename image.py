from PIL import Image

mac = Image.open("example.jpg")
mac.show()
mac.size
mac.filename
mac.format_description
mac_crop = mac.crop((0, 0, 100, 100))
mac.paste(im=mac_crop, box=(0, 0))
mac.resize((3000, 500))
mac.rotate(90)
mac.putalpha(255)  # alpha ranges from 0 (transparent) to 255 (opaque)
mac.save("multi_mac.png")
pencil = Image.open("pencil.jpg")
print(pencil.size)
x, y = 0
w = 1950 / 3
h = 1300 / 10
pencil.crop((x, y, w, h))
