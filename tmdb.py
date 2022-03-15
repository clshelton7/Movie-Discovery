# pylint: disable=C0114, C0116, C0103, W0702, R0914, W0622
import os
import random
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # KEY from .env


def get_movie_data():
    broken = []  # found broken id pages are stored here upon running

    while True:  # condition for try except
        movie_ids = [
            # hardcoded for testing and comment displays for milestone 2
            str(585),
            str(114),
            str(157336),
            str(505948),
            str(405774),
        ]
        # check if there are any broken ids, then remove them from the id list
        if broken:
            for id in broken:
                movie_ids.remove(id)

        # randomly select a movie to display information about
        movieID = movie_ids[random.randint(0, len(movie_ids) - 1)]

        BASE_URL = "https://api.themoviedb.org/3/movie/" + movieID

        params = {
            "api_key": os.getenv("KEY"),
        }

        tmdb_response = requests.get(BASE_URL, params=params)
        data = tmdb_response.json()

        movies = data

        try:
            # get title string from json
            def get_single_element(movie):
                return movie

            # get genre strings from json
            def get_genre(movie):
                return movie["name"]

            # add necessary path
            def get_photos(movie):
                return "https://image.tmdb.org/t/p/original" + movie

            # get information through map
            titles = map(get_single_element, [movies["original_title"]])
            genres = map(get_genre, movies["genres"])
            photos = map(get_photos, [movies["backdrop_path"]])
            taglines = map(get_single_element, [movies["tagline"]])

            return {
                "titles": list(titles),
                "genres": list(genres),
                "photos": list(photos),
                "tags": list(taglines),
                "id": movieID,  # return id element, rather than list
            }

        except:
            broken.append(movieID)  # remove broken id page from results
            continue


def get_title_by_id(movieID):
    BASE_URL = "https://api.themoviedb.org/3/movie/" + movieID

    params = {
        "api_key": os.getenv("KEY"),
    }

    tmdb_response = requests.get(BASE_URL, params=params)
    data = tmdb_response.json()
    return data["original_title"]


get_movie_data()
