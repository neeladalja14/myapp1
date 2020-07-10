import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://wallpapercave.com/wp/TuVhQdr.jpg")

print("Status code: ", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image" + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save images.")





"""params = {"q": "pizza"}

r = requests.get("http://www.bing.com/search", params=params)

print("Status: ", r.status_code)

print(r.url)

f = open("./page.html", "w+")
f.write(r.text)"""