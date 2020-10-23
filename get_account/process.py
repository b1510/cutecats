from instagrapi import Client

ACCOUNT_USERNAME = "cutecats_cm"
ACCOUNT_PASSWORD = "JcbzAntho12.Cutecats"

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

cl.album_upload(
    ["data/tests/0c2b3cfd-6ad4-4ccd-bb32-b4c200cd03d5.jpg",
     "data/tests/1c0e644f-6eae-4712-82db-6a4a453ef7d6.jpg"], caption="First post")
