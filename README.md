# SIG-to-GoogleCalendar

## A python script to get class schedules on UFLA's SIG and convert to a .CSV file to use in Google Calendar

### Prerequisites

What you need to run this script

```
Python 3.x.x

Beautiful Soup 4
pip install beautifulsoup4

Numpy
pip install numpy

urllib3
pip install urllib3
```

### Running

Just run 

``` python3 sigToCalendar.py ```

You'll need to provide some information to run this script

* Login - Your SIG's login
* Password - Your SIG's password
* Start Date - From which day do you want to replicate your schedules
* End Date - Until which day do you want to replicate your schedules

After that, a .csv file will be generated. Just go to "calendar.google.com > Import > Select file from your computer" and choose the .csv file.

It's strongly recommended to create a new calendar to import the .csv file

### Contributing

Feel free to give any feedback, open new issues or pull requests
