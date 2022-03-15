# pylint: disable=C0114, C0116, C0103, W0613, W0611
import requests
import tmdb
from tmdb import get_movie_data


def getWiki(movie_title):
    BASE_URL = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": movie_title,
        "prop": "info",
        "inprop": "url",
    }
    wiki = requests.get(BASE_URL, params=params)
    data = wiki.json()
    pages = data["query"]["pages"]

    # access url from values in json
    def getLink(movie):
        for key in pages.values():
            return key["fullurl"]

    link = [getLink(pages)]
    return {"link": list(link)}
