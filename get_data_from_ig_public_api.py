import requests
import uuid
import os


HASHTAG = "cats"
BASEPATH_FOLDER = "data"


def create_dir(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def save_image_from_link(image_url):

    create_dir("{}/{}".format(BASEPATH_FOLDER, HASHTAG))
    img_data = requests.get(image_url).content
    with open('data/{}/{}.jpg'.format(HASHTAG, uuid.uuid4()), 'wb') as handler:
        handler.write(img_data)


class Parser:
    HASH_KEY = "graphql"
    HASHTAG_KEY = "hashtag"
    MEDIA_KEY = "edge_hashtag_to_media"
    LIST_KEY = "edges"
    NODE_KEY = "node"
    CAPTION_LIST_KEY = "edge_media_to_caption"
    TEXT_KEY = "text"
    URL_KEY = "display_url"

    def __init__(self, tag):
        self.tag = tag

    def get_url(self):
        url = "https://www.instagram.com/explore/tags/" + self.tag + "/?__a=1"
        return url

    def get_request_response(self):
        r = requests.get(url=self.get_url(), params="")
        data = r.json()
        return data

    def get_images(self):
        data = self.get_request_response()
        nodes_list = data[Parser.HASH_KEY][Parser.HASHTAG_KEY][Parser.MEDIA_KEY][Parser.LIST_KEY]
        for obj in nodes_list:
            url = obj[Parser.NODE_KEY][Parser.URL_KEY]
            if len(url) > 0:
                save_image_from_link(url)


def main():
    parser = Parser(HASHTAG)
    parser.get_images()


if __name__ == "__main__":
    main()
