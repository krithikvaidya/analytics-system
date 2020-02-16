import json  # to convert our dict into the JSON format
from django.utils import timezone  # to get the date of the request


class LogsAppMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):

        # TODO: save logs only for requests to the homepage.

        # the dictionary that will hold the event log
        event_log = {}

        # get the username of the user making the request
        # if not logged in, kept empty
        username = ''
        if request.user.is_authenticated:
            username = request.user.username
        event_log['user'] = username

        # get the client's IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        event_log['ip_address'] = x_forwarded_for.split(
            ',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
        event_log['method'] = request.method

        # get name of browser used to make the request
        event_log['browser_info'] = request.META['HTTP_USER_AGENT']

        # TODO: get location based on IP address
        event_log['location'] = ''

        # Timestamp of event
        event_log['timestamp'] = str(timezone.now())

        # TODO: store insensitive GET/POST request information
        event_log['data'] = str(request)

        try:
            with open('logs.json', 'a', encoding='utf-8') as f:
                json.dump(event_log, f, ensure_ascii=False, indent=4)

        except OSError:
            print('Could not open logs JSON file for writing.')

        response = self.get_response(request)
        return response
