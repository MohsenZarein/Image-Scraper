from bs4 import BeautifulSoup
import requests
from io import BytesIO
from PIL import Image
import os


def SearchForImage():

    search = input("Search for:")
    params = {"q":search}
    directory_name = search.replace(' ','_')

    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)

    req = requests.get("https://www.bing.com/images/search",params=params)
    #print(req.status_code)

    soup = BeautifulSoup(req.text,"html.parser")
    link = soup.findAll("a",{"class":"thumb"})

    for item in link:
        try:
            imgObj = requests.get(item.attrs["href"])
            print("Getting ",item.attrs["href"],"...")
            title = item.attrs["href"].split('/')[-1]
            try:
                image = Image.open(BytesIO(imgObj.content))
                image.save("./" + directory_name + "/" + title, image.format)
            except:
                print("could not save image")
        except:
            print("Could not reach a website ...")
    SearchForImage()

SearchForImage()


