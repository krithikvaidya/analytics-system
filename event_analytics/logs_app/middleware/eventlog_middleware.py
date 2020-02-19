import json  # to convert our dict into the JSON format
from django.utils import timezone  # to get the date of the request
from simple_geoip import GeoIP
from datetime import datetime, timezone

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

        # get location based on ip
        geoip = GeoIP("at_w3VVriiq1AGRdxPb0bYZIhhR8KoxL")
        data = geoip.lookup(ip)
        event_log['location'] = data['location']['city']

        # Timestamp of event
        event_log['timestamp'] = str(datetime.now(timezone.utc))

        # TODO: store insensitive GET/POST request information
        headers = ''
        for header, value in request.META.items():
            if not header.startswith('HTTP'):
                continue
            header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
            headers += '{}: {}\n'.format(header, value)

        meta = request.META['CONTENT_TYPE']
        ct = request.META['CONTENT_TYPE']
        # print(f'{request.method} HTTP/1.1\nContent-Length: {meta}\nContent-Type: {ct}\n{headers}\n\n{request.body}')
       
        # append the above log to the JSON file
        try:
            with open('logs.json', 'a', encoding='utf-8') as f:
                json.dump(event_log, f, ensure_ascii=False)
                f.write('\n')

        except OSError:
            print('Could not open logs JSON file for writing.')

        response = self.get_response(request)
        return response
