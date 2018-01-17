import json
from pathlib import Path
import urllib.request as request
from threading import Thread
import timeout_decorator

IMAGE_DIR = './images/'
DATA_DIR = './data_json/'


@timeout_decorator.timeout(3)
def url_check(url, id):
    print('with id =' + str(id) + 'checking url ' + url)
    try:
        if request.urlopen(url).code == 200:
            return True
        else:
            return False
    except:
        print('error')
        return False


# f=url_check('https://www.google.com')


def download_images(url, id):
    """
    image download and save
    :return: id
    """
    print('downloading image with id ' + str(id))
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


# download_images('https://d3g1cn7w902vur.cloudfront.net/SeriesAHome/reg2.jpg', 1)
# sample json
# {'url': ['http://www.dhresource.com/0x0s/f2-albu-g3-M01-BD-6F-rBVaHFSH-veAFIYuAAG3p06S-ig068.jpg/fashion-golden-sexy-night-club-dress-hollow.jpg', 'https://www.dhresource.com/0x0/f2/albu/g3/M01/BD/6F/rBVaHFSH-veAFIYuAAG3p06S-ig068.jpg', 'https://www.dhresource.com/0x0s/f2-albu-g3-M01-BD-6F-rBVaHFSH-veAFIYuAAG3p06S-ig068.jpg/fashion-golden-sexy-night-club-dress-hollow.jpg'], 'imageId': '42029'}


def train_json_decode(fp):
    """
    download images

    :param fp:
    :return: 1
    """
    print('in train json decode')
    urls = []
    imageIds = []
    with open(fp) as json_data:
        data = json.load(json_data)
        print(data.keys())
        for images in data['images']:
            for url in images['url']:
                # if url_check(l, images['imageId']):
                urls.append(url)
                imageIds.append(images['imageId'])
                print(url, images['imageId'])
                Thread(target=download_images, args=(url, images['imageId'])).start()
            # download_images(l, images['imageId'])
            # break
            # else:
            # continue

    return urls, imageIds


if __name__ == "__main__":
    print('in main class')
    x, y = train_json_decode('data_json/train.data.json')
