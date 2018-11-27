'''
Set up the Falcon-based web API. To learn more about Falcon, please see:
https://falconframework.org/
'''

import falcon
from falcon_openapi import OpenApiRouter

# load from file
application = app = falcon.API(
    router=OpenApiRouter(file_path='openapi-spec.yaml')
)
