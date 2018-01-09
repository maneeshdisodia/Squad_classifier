import json
import os
from pathlib import Path
import urllib.request as request

IMAGE_DIR = './images/'


def download_images(url, id):
    """
    image download and save
    :return: id
    """
    file_name = IMAGE_DIR + str(id) + '.jpg'
    my_file = Path(file_name)
    try:
        my_file.resolve()
        if my_file.exists():
            print('file exists')
            return 0
        else:
            print('downloading ' + file_name)
            request.urlretrieve(url, file_name)
            return 1

    except:  # doesn't exist
        print('error' + str(id))
        return -1




download_images('https://d3g1cn7w902vur.cloudfront.net/SeriesAHome/reg2.jpg', 1)


def id_to_imageCheck():
    """check for image already donloded
    :return:boolean
    """
    pass
