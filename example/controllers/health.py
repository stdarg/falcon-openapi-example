'''
Application logic for the /health route.
The "/health" route should have no version or prefix in the path.
'''

import falcon
import json

# Because every controller is required by falcon-api, we need to qualify our
# modules with our module name, 'test'
from example.__version__ import __version__, __git_hash__


class HealthCheck(object):
    def on_get(self, req, resp):
        doc = {
            'name': 'Test Service',
            'version': __version__,
            'git_hash': __git_hash__
        }

        # Format the response in JSON
        resp.content_type = falcon.MEDIA_JSON

        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned.
        resp.status = falcon.HTTP_200
