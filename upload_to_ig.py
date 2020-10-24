from instagrapi import Client
import os
from dotenv import load_dotenv
load_dotenv()

ACCOUNT_USERNAME = os.getenv('ACCOUNT_USERNAME')
ACCOUNT_PASSWORD = os.getenv('ACCOUNT_PASSWORD')
BASEPATH_FOLDER = "data/"
CURRENT_FOLDER = BASEPATH_FOLDER + "current/"
ERRORS_FOLDER = BASEPATH_FOLDER + "errors/"
CAPTION = "Hello cuttie !!! follow @" + ACCOUNT_USERNAME


def folder_to_list(folder):
    list_of_files = [f for f in os.listdir(folder) if f.endswith(".jpg")]
    return list_of_files


def create_dir(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


class UploadToIG:

    def __init__(self, folder_one, folder_two):
        self.folder_one = folder_one
        self.folder_two = folder_two
        self.list_files_one = folder_to_list(folder_one)
        self.list_files_two = folder_to_list(folder_two)

        self.cl = Client()
        self.cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

        create_dir(CURRENT_FOLDER)
        create_dir(ERRORS_FOLDER)

    def upload(self, image_one, image_two, caption):
        self.cl.album_upload(
            [image_one,
             image_two], caption=caption)

    def process(self):
        while self.list_files_one:

            # take first element
            file_one = self.list_files_one[0] if self.list_files_one else None
            file_two = self.list_files_two[0] if self.list_files_two else None

            # move it to the current folder
            img_one = CURRENT_FOLDER + file_one
            img_two = CURRENT_FOLDER + file_two
            os.replace(self.folder_one + file_one, img_one)
            os.replace(self.folder_two + file_two, img_two)

            del(self.list_files_one[0])
            del(self.list_files_two[0])

            # upload to IG
            try:
                self.upload(image_one=img_one, image_two=img_two, caption=CAPTION)
            except:
                os.replace(img_one, ERRORS_FOLDER + file_one)
                os.replace(img_two, ERRORS_FOLDER + file_two)


def main():
    utig = UploadToIG(folder_one=BASEPATH_FOLDER + "cats/", folder_two=BASEPATH_FOLDER + "cm/")
    utig.process()


if __name__ == "__main__":
    main()

