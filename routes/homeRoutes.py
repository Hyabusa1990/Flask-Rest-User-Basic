from flask_restful import Api
from resources.homeRessource import HomeListResource


def homeRoutes(api: Api, baseurl: str):
    api.add_resource(HomeListResource, baseurl)

