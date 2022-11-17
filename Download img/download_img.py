import random
import requests
import json
import threading

def download_photo(url_, name_of_img="photo", format_img="jpg"):
    '''
    Download image using url. Input url, name of image, format img.
    :param url_:

    :param name_of_img:
    :param format_img:
    :return:
    '''
    try:
        get_img = requests.get(str(url_))
    except Exception as err:
        print(f"Something is wrong {err}")
        return

    if get_img.status_code == 200:
        with open(f"{name_of_img}.{format_img}", "wb") as photo:
            photo.write(get_img.content)
        return "Success download"

with open("img_list.json", "r") as file:
    data = json.load(file)
    for i in data:
        download_photo(i, random.randint(1, 100))
