import json  # to convert our dict into the JSON format


class LogsAppMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):

        # TODO: save logs only for requests to the homepage.
        
        response = self.get_response(request)
        return response