Cabot Plivo Plugin
=====

This is an alert plugin for the cabot service monitoring tool. It allows you to alert users by Plivo sms.

## Installation
Enter the cabot virtual environment.
    $ pip install cabot-alert-plivo
    $ foreman stop
Add cabot_alert_plivo to the installed apps in settings.py
    $ foreman run python manage.py syncdb
    $ foreman start