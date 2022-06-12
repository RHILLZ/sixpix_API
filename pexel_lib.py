import os
import requests
import webbrowser
from pprint import pprint


# API KEY FROM PEXELS.COM STORED IN ENV VARIABLES
key = os.getenv('PEXEL_API_KEY')

# INPUT FOR PICTURE I WANT TO SEARCH FOR
# query = input('What do you want a picture of? ')

# PEXELS API BASE URL WITH HEADERS
base_url = "https://api.pexels.com/v1/search?query="
headers = {
    "Content-Type": "application/json",
    "Authorization": key
}
pp = '&per_page=6'

# The initial photos that are returned from the search
# The next page url returned from the initial query abd the page number

next_page = ''

# photos, next_page_url, page = ()


def sortImages(photos: list):
    images = []
    for photo in photos:
        images.append(photo['src']['original'])
    return images


def searchQuery(query):
    res = requests.get(base_url+query+pp, headers=headers)
    photos = res.json()['photos']
    images = sortImages(photos)
    next_page = res.json()['next_page']
    page_num = res.json()['page']
    return (images, next_page, page_num)


# Function to goto the next page
def goToNextPage(url):
    response = requests.get(url, headers=headers)
    photos = response.json()['photos']
    images = sortImages(photos)
    nextPage = response.json()['next_page']
    pageNum = response.json()['page']
    return (images, nextPage, pageNum)

 # Saves image to the Downloads folder


def saveImage(filename: str, image: str):
    img = requests.get(image)
    path = '/Users/rhillx/Downloads'
    name = os.path.join(path, filename+'.jpeg')
    try:
        with open(name, 'wb') as f:
            f.write(img.content)
        return True
    except:
        return False


# while True:
#     images = []
#     for photo in photos:
#         images.append(photo['src']['original'])
#         pprint(f"{page} " + photo['src']['original'])
#     ans = input("see more? ")
#     if ans == 'y':
#         photos, next_page_url, page = goToNextPage(next_page_url)
#     if ans == 'n':
#         imageNum = int(input('which image do you want to download? '))
#         image = requests.get(images[imageNum])
#         path = '/Users/rhillx/Downloads'
#         filename = input('what would you like to name this file? eg(*.jpeg) ')
#         name = os.path.join(path, filename+'.jpeg')
#         with open(name, 'wb') as f:
#             f.write(image.content)
#         print(f"Your file is saved here: {name}")
#         break
