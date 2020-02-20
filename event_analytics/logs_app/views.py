from django.shortcuts import render
from datetime import datetime, timezone
from dateutil.parser import parse

import json

def index(request):
    """Renders the homepage

    The logging of event is done in the custom middleware
    (eventlog_middleware.py) itself. This view simply renders
    the index page
    """

    return render(request, 'logs_app/index.html')

def visualize(request):
    """Visualize the Event Logs

    Visualizes the following data:
    1. Total page visits
    2. Page visits in the past day
    3. Page visits in the past week
    4. Page visits in the past year
    5. Page visits filtered by location

    """

    location = None  # stores location filter
    loc_visitors = 0  # stores visitor count by location
    style = "display: none;"  # whether or not to display the location-based chart
    
    # if the request has been created for visualizing data by location,
    if 'location' in request.POST:
        location = request.POST['location']
        style = "display: block;"

    try:
        
        with open('logs.json', 'r', encoding='utf-8') as f:

            total_visitors = 0
            year_visitors = 0
            week_visitors = 0
            day_visitors = 0

            for line in f:
                
                line = line.strip()

                if not line:  # break if we have reached the end of the file
                    break
                
                total_visitors += 1

                # convert JSON object to python dict using json.loads()
                event_log = json.loads(line)

                # get the time difference between now and time of event log creation
                past_date = parse(event_log['timestamp'])
                difference = datetime.now(timezone.utc) - past_date

                if difference.days == 0:  # request made in the past day
                    year_visitors += 1
                    week_visitors += 1
                    day_visitors += 1

                elif difference.days <= 6:  # request made in the past week
                    week_visitors += 1
                    year_visitors += 1

                elif difference.days <= 364:  # request made in the past year
                    year_visitors += 1

                # if the location of this log matches the filter, increment number
                # of visitors from that location
                if location:
                    if event_log['location'] == location:
                        loc_visitors += 1


    except OSError:
        print('Could not open logs JSON file for reading.')


    # data to be sent to the template
    context = {
        'day': day_visitors,
        'week': week_visitors,
        'year': year_visitors,
        'total': total_visitors,
        'loc_visitors': loc_visitors,
        'location': location,
        'style': style 
    }

    return render(request, 'logs_app/visualize.html', context)

    
def logged_out(request):
    """Renders the logged out page"""

    return render(request, 'logs_app/logged_out.html')
        