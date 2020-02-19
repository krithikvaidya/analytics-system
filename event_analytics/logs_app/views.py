from django.shortcuts import render
from datetime import datetime, timezone
from dateutil.parser import parse

import json

def index(request):

    try:
        
        with open('logs.json', 'r', encoding='utf-8') as f:

            total_visitors = 0
            year_visitors = 0
            week_visitors = 0
            day_visitors = 0

            for line in f:
                
                line = line.strip()

                if not line:
                    break
                
                total_visitors += 1

                event_log = json.loads(line)
                past_date = parse(event_log['timestamp'])

                print(type(past_date))
                difference = datetime.now(timezone.utc) - past_date

                if difference.days == 0:

                    year_visitors += 1
                    week_visitors += 1
                    day_visitors += 1

                elif difference.days == 6:

                    week_visitors += 1
                    day_visitors += 1

                elif difference.days == 0:

                    day_visitors += 1


    except OSError:
        print('Could not open logs JSON file for reading.')

    context = {'day': day_visitors,
               'week': week_visitors,
               'year': year_visitors }

    return render(request, 'logs_app/index.html', context)

# def visualize(request):

    

        