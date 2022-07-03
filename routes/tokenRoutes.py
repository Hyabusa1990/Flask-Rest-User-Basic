from flask_restful import Api
from resources.tokenResource import TokenResource, RefreshResource


def tokenRoutes(api: Api, baseurl: str):
    api.add_resource(TokenResource, baseurl)
    api.add_resource(RefreshResource, baseurl + '/refresh')
