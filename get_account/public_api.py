import requests


class Parser:
    HASH_KEY = "graphql"
    HASHTAG_KEY = "hashtag"
    MEDIA_KEY = "edge_hashtag_to_media"
    LIST_KEY = "edges"
    NODE_KEY = "node"
    CAPTION_LIST_KEY = "edge_media_to_caption"
    TEXT_KEY = "text"

    def __init__(self, tag):
        self.tag = tag

    def get_url(self):
        url = "https://www.instagram.com/explore/tags/" + self.tag + "/?__a=1"
        return url

    def get_request_response(self):
        r = requests.get(url=self.get_url(), params="")
        data = r.json()
        return data

    #data['graphql']['hashtag']['edge_hashtag_to_media']['edges'][0]['node']['display_url']
    def get_captions(self):
        captions = []
        data = self.get_request_response()
        nodes_list = data[Parser.HASH_KEY][Parser.HASHTAG_KEY][Parser.MEDIA_KEY][Parser.LIST_KEY]
        for obj in nodes_list:
            caption_list = obj[Parser.NODE_KEY][Parser.CAPTION_LIST_KEY][Parser.LIST_KEY]
            if len(caption_list) > 0:
                caption = caption_list[0][Parser.NODE_KEY][Parser.TEXT_KEY]
                captions.append(caption)
                print(caption)


def main():
    parser = Parser("cats")
    parser.get_captions()


if __name__ == "__main__":
    main()
