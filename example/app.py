'''
Set up the Falcon-based web API. To learn more about Falcon, please see:
https://falconframework.org/
'''

import falcon
from falcon_openapi import OpenApiRouter

# load from file
openapi_router = OpenApiRouter(file_path='openapi-spec.yaml')

# gunicorn requires the global be named 'application'
application = falcon.API(router=openapi_router)
