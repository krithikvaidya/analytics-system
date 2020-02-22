# Spoken Tutorial Event Logs and Analytics System

## Requirements
Python3.5+ and Pip (Rest of the dependencies will be installed below)

## Quick Setup

### Clone this repository
```
git clone https://github.com/krithikvaidya/analytics-system.git
```

### Change directory
```
cd analytics-system
```

### Install virtualenv and virtualenvwrapper to isolate dependencies *(Optional, but recommended)*
##### 1. Ubuntu
```
sudo apt install python3-venv virtualenvwrapper
```
##### 2. Windows
```
pip3 install virtualenvwrapper-win
```

### Create the virtualenv
##### 1. Ubuntu
```
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
mkvirtualenv -p /usr/bin/python3 -a $PWD -r requirements.txt logs_app
```
##### 2. Windows
```
mkvirtualenv -a . -r requirements.txt logs_app
```

### Manually Install requirements (only if not using virtualenv)
```
pip3 install -r requirements.txt
```

### Change into Django project directory
```
cd event_analytics/
```

### Run database migrations
``` 
python3 manage.py migrate
```

The app is now ready for use use!  
Run the app with  
```
python3 manage.py runserver
```

and open up your browser window at *http://localhost:8000/* to use the app.  

### User Accounts
If you wish to work with user accounts, first create a *superuser*
```
python3 manage.py createsuperuser
```
Then, you can create other user accounts from the Django admin page, if required.


## Overview of the Project

The project was created with a view of *keeping things simple, while fulfilling all requirements.*

## High Level Explanation

The Django project (named *event_analytics*) contains an app called *logs_app* that handles the recording of event logs and rendering their visualizations.

#### Middleware
For creating and saving event logs on each visit to the homepage, a custom Django middleware (can be found in *logs_app/middleware/eventlog_middleware*) was used. A Django middleware is like a plug-in that we can hook into the Django's request/response cycle. Thus, it is the natural solution to use for saving user event logs. For this purpise, Django's [new style](https://raturi.in/blog/understand-and-create-custom-django-middleware/) middleware (Django 2.0+) has been used.  
The event info is extracted from the *request* object and then saved in the JSON format (currently, the logs can be found in *logs.json*).

#### Information Stored
The following event-related information is being saved in Activity Logs:

* 1. Username
* 2. IP Address
* 3. Request Method
* 4. Browser Info
* 5. Location of Request
* 6. Timestamp
* 7. Other insensitive request information

#### User Account System
The user account system has been kept simple: Registrations can be done only through the Django admin page. A separate page on the website has been kept for logging in and logging out. Django's default [Authentication system](https://docs.djangoproject.com/en/3.0/topics/auth/) has been used for this purpose.

#### Extracting Location From IP
The current setup gets the user's location from their IP address by querying an external API. To map the client's IP address to their location, we use the [simple-geoip](https://pypi.org/project/simple-geoip/) Python library. This library uses the free [GeoIPify](https://ip-geolocation.whoisxmlapi.com/api) API to get the client's city from the IP address of their request.  

#### Visualizations with Highcharts
The [Highcharts](https://www.highcharts.com/) Javascript library has been used to efficiently create simple visualizations with minimal effort. Two types of visualizations are available in this setup:
* 1. Visualizations based on **Time** (Number of visits in the past day/week/year or all time)
* 2. Visualizations based on **Location** (Number of visits from a given city)

#### Front End Design
For the front-end of the website, the Django templating language has been used to construct the HTML structure of the page. [Bootstrap](https://getbootstrap.com/) has been used extensively, along with basic CSS and Javascript for cosmetic appeal and screen-size responsiveness.

The implementation details of the above features can be understood by reading through the code and inline documentation.

## Notes and Improvements
* Ideally, the generation and saving of event logs with each visit should be done asynchronously, on worker threads separate from the main Django process. This is because we do not want the overhead of storing logs to slow down the website and interfere with the user experience. Hence, there is a slight delay in loading the homepage in the current setup, where the middleware requests the GeoIP API to map the user's IP address to their location, and waits for this response.  
* The above delay of querying the *GeoIPify* API can be avoided if the website was allowed to support the [HTML5 Geolocation API](https://www.w3schools.com/html/html5_geolocation.asp). The overhead of translating IP address to Location would be avoided. 
* The login system has been kept fairly minimal. User registration is done indirectly through the Django admin page.

## Standards
* Git commit messages strictly adhere to the style mentioned in [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
* The .gitignore file for this project is partially taken from [here](https://www.gitignore.io/api/django)
* Docstrings follow [PEP257](https://www.python.org/dev/peps/pep-0257/) conventions  

Created By:  
Krithik Vaidya  
B.Tech, 2nd Year (Information Technology)    
NITK Surathkal  