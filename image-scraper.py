from bs4 import BeautifulSoup
import requests
from io import BytesIO
from PIL import Image

search = input("Search for:")
params = {"q":search}

req = requests.get("https://www.bing.com/images/search",params=params)
print(req.status_code)

soup = BeautifulSoup(req.text,"html.parser")
link = soup.findAll("a",{"class":"thumb"})

path = "/home/mohsen/VSCode/ImageScraper/scraped_image/"

for item in link:
    try:
        imgObj = requests.get(item.attrs["href"])
        print(imgObj.status_code)
        print("Getting ",item.attrs["href"],"...")
        title = item.attrs["href"].split('/')[-1]

        try:
            image = Image.open(BytesIO(imgObj.content))
            image.save(path + title , image.format)
        except:
            print("could not save image")
    except:
        print("connection failed")



