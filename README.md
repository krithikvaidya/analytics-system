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
http://127.0.0.1:8000/
```
to use the app.  

If, at anytime, you wish to re-enter the virtual environment after closing it, use
```
workon logs_app
```

## Overview of the Project

* The project was created with a view of *keep things simple, while fulfilling all requirements*

### Django Project Structure
The Django project (named *event_analytics*) contains an app called *logs_app* that

A Django middleware is like a plug-in that you can hook into the Django's request/response cycle. Thus, it is the natural solution to use for saving user event logs.

With the view of maintaining simplicity, we haven't saved the event logs asynchronously, on threads separate from the main Django web-app process (which should ideally be done, so that the main Django app does not slow down due to this activity). Hence, there is a slight delay in loading the homepage, where the middleware requests the GeoIP API to map the user's IP address to their location, and waits for this response.

The user account system has been kept simple: Registrations can be done only through the Django admin page. A separate page on the website has been kept for logging in and logging out.

To map the client's IP address to their location, we use the [simple-geoip](https://pypi.org/project/simple-geoip/) Python library. This library uses the free [GeoIPify](https://ip-geolocation.whoisxmlapi.com/api) API to get the client's city from the IP address of their request.  

The [Highcharts](https://www.highcharts.com/) Javascript library has been used to efficiently create simple visualizations with minimal effort.

Bootstrap has been used for the front-end

The logs are stored in *logs.json* in the root project directory

## Notes
* Git commit messages strictly adhere to the style mentioned in [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
* The .gitignore file for this project is partially taken from [here](https://www.gitignore.io/api/django)
* Docstrings follow [PEP257](https://www.python.org/dev/peps/pep-0257/) conventions  

Created By:  
Krithik Vaidya,  
B.Tech 2nd Year (Information Technology),   
NITK Surathkal  