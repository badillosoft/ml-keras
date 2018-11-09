from PIL import Image
import requests
from StringIO import StringIO

url = "https://news.nationalgeographic.com/content/" + \
    "dam/news/2018/05/17/you-can-train-your-cat/" + \
    "02-cat-training-NationalGeographic_1484324." + \
    "ngsversion.1526587209178.adapt.1900.1.jpg"

response = requests.get(url)

im = Image.open(StringIO(response.content))

im = im.resize((32, 32), Image.NEAREST)

im.save("2.png", "PNG")