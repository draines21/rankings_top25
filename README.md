TOP 25 SCORING ENGINE:
This is basic Top 25 College Football scoring resume engine to be used and outputted to the command line.
Takes into account certain weighted criteria(which are defined in resume_weights.py) like ranked wins and penalizes losses. As well as scores on margin of victoy per 6 points, and even conference strength.
The weights are tunable if you like to change them in the resume_weights.py file.

SETUP INSTRUCTIONS:

Recommended to use a virtual environment:
python3 -m venv venv
source venv/bin/activate MAC/LINUX
venv/Scripts/activate WINDOWS

To use this you need to go Collegefootballdata.com and request an API KEY.
Clone this repo to local machine.
Add API KEY to config file.
Caching helpers are included to reduce API calls
Install the requests library with: pip install requests
Run project from command line with python3 main.py

This project was built as a learning exercise for Boot.dev
