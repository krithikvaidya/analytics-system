# Spoken Tutorial Event Logs and Analytics System

### Requirements
Python 3 and Pip 3

## Quick Setup

### Clone this repository
```
git clone https://github.com/krithikvaidya/analytics-system.git
```

### Change directory
```
cd analytics-system
```

### Install virtualenv and virtualenvwrapper to isolate dependencies
#### (Optional, but recommended)
```
sudo apt install python3-venv virtualenvwrapper
```

### Create the virtualenv
```
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
mkvirtualenv -p /usr/bin/python3 -a $PWD logs_app
```

### Install dependencies from the requirements file
```
pip3 install -r requirements.txt
```

### Change into Django project directory
```
cd event_analytics/
```

### Run database migrations for the Django app
``` 
python3 manage.py migrate
```

The app is now ready for use use!  
Run the app with  
```
python3 manage.py runserver
```

Open up your browser window at
```
http://localhost:8000/
```
to use the app.  

If, at anytime, you wish to re-enter the virtual environment after closing it, use
```
workon logs_app
```

## Overview of the Project

* The project was created with a view of *keeping things simple, while fulfilling all requirements*

### High Level Explanation

The Django project (named *event_analytics*) contains an app called *logs_app* that handles the recording of event logs and rendering their visualizations.

For creating and saving event logs on each visit to the homepage, a custom Django middleware (can be found in *logs_app/middleware/eventlog_middleware*) was used. A Django middleware is like a plug-in that we can hook into the Django's request/response cycle. Thus, it is the natural solution to use for saving user event logs.
The log info is extracted from the *request* object and then saved in the JSON format (currently, the logs can be found in *logs.json*).

The following event-related information is being saved in Activity Logs:

> 1. Username
> 2. IP Address
> 3. Request Method
> 4. Browser Info
> 5. Location of Request
> 6. Timestamp
> 7. Other insensitive request information

The user account system has been kept simple: Registrations can be done only through the Django admin page. A separate page on the website has been kept for logging in and logging out. Django's default [Authentication system](https://docs.djangoproject.com/en/3.0/topics/auth/) has been used for this purpose.

The current setup gets the user's location from their IP address by querying an external API. If having location access in the browser was permitted, we would be able to get the user's location much more easily and quickly. To map the client's IP address to their location, we use the [simple-geoip](https://pypi.org/project/simple-geoip/) Python library. This library uses the free [GeoIPify](https://ip-geolocation.whoisxmlapi.com/api) API to get the client's city from the IP address of their request.  

The [Highcharts](https://www.highcharts.com/) Javascript library has been used to efficiently create simple visualizations with minimal effort. Two types of visualizations are available in this setup:
* 1. Visualizations based on **Time** (Number of visits in the past day/week/year or all time)
* 2. Visualizations based on **Location** (Number of visits from a given city)

For the front-end of the website, the Django templating language has been used to construct the HTML structure of the page, and for sending data from the views to the templates. Bootstrap has been used extensively along with basic CSS and Javascript for cosmetic appeal and screen-size responsiveness.

The implementation details of the above features can be understood by reading through the code and internal documentation.

## Notes and Extensions to the Project
* With the view of maintaining simplicity, we haven't saved the event logs asynchronously, on threads separate from the main Django web-app process (which should ideally be done, so that the main Django app does not slow down due to this activity). Hence, there is a slight delay in loading the homepage, where the middleware requests the GeoIP API to map the user's IP address to their location, and waits for this response.  
* The current setup gets the user's location from their IP address by querying an external API. If having location access in the browser was permitted, we would be able to get the user's location much more easily and quickly.
* The login system has been kept fairly minimal, to maintain simplicity. User registration is done indirectly through the Django admin page or the command line.

## Standards
* Git commit messages strictly adhere to the style mentioned in [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
* The .gitignore file for this project is partially taken from [here](https://www.gitignore.io/api/django)
* Docstrings follow [PEP257](https://www.python.org/dev/peps/pep-0257/) conventions  

Created By:  
Krithik Vaidya  
B.Tech, 2nd Year (Information Technology)    
NITK Surathkal  