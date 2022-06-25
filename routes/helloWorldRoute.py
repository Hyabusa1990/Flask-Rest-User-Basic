from flask_restful import Api
from resources.helloWorldRes import HelloWorldListResource


def helloWorldRoutes(api: Api, baseurl: str):
    api.add_resource(HelloWorldListResource, baseurl)

