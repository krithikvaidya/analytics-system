# Spoken Tutorial Event Logs and Analytics System

### Requirements
Python 3 and Pip 3

## Quick Setup

### Clone this repository
```
git clone https://github.com/krithikvaidya/analytics-system.git`
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



Created By:
Krithik Vaidya,
B.Tech 2nd Year (Information Technology), 
NITK Surathkal