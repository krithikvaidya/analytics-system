import json  # to convert our dict into the JSON format
from simple_geoip import GeoIP  # for converting IP to location
from datetime import datetime, timezone
from django.urls import resolve  # to resolve current URL


class LogsAppMiddleware(object):
    """Middleware definition for recording event logs

    This is a custom middleware that scrapes event log data from the
    request object and stores it in a JSON file.
    Event logs for the homepage ONLY are stored.
    """

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):

        # if the current URL is not the home page, do not record event log
        current_url = resolve(request.path_info).url_name
        if not current_url == 'index':
            response = self.get_response(request)
            return response

        # the Python dictionary that will hold the event log
        event_log = {}

        # get the username of the user making the request.
        # if not logged in, kept empty
        username = ''
        if request.user.is_authenticated:
            username = request.user.username
        event_log['user'] = username

        # get the client's IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        elif request.META.get('HTTP_X_REAL_IP'):
            ip = request.META.get('HTTP_X_REAL_IP')
        else:
            ip = request.META.get('REMOTE_ADDR')

        event_log['ip_address'] = ip

        # get method of request (GET, POST, etc)
        event_log['method'] = request.method

        # get name of browser used to make the request
        event_log['browser_info'] = request.META['HTTP_USER_AGENT']

        # get location (city) based on ip using Simple-GeoIP
        # https://pypi.org/project/simple-geoip/
        geoip = GeoIP("at_w3VVriiq1AGRdxPb0bYZIhhR8KoxL")
        data = geoip.lookup(ip)
        event_log['location'] = data['location']['city']
        request.session['location'] = event_log['location']

        # Timestamp of event
        event_log['timestamp'] = str(datetime.now(timezone.utc))

        # store insensitive GET request information (POST requests are not supported on this webpage)

        # request.headers supported in Django 2.2+
        other_info = dict(request.headers)

        keys_to_remove = ["Cookie", "csrftoken"]
        for key in keys_to_remove:
            other_info.pop(key, None)

        other_info = str(other_info)

        event_log['other_info'] = other_info

        # append the above log to the JSON file. Report error
        # if the file could not be appended to, and continue
        # loading the page normally.
        try:
            with open('logs.json', 'a', encoding='utf-8') as f:
                json.dump(event_log, f, ensure_ascii=False)
                f.write('\n')

        except OSError:
            print('Could not open logs JSON file for writing.')

        # store the event_log in the session, so that it can be accessed by the view
        request.session['event_log'] = event_log

        response = self.get_response(request)
        return response
