from PIL import Image

im = Image.open("iot.jpg")

im = im.resize((32, 32), Image.NEAREST)

im.save("1.png", "PNG")