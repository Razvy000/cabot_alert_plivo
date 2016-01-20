Cabot Plivo Plugin
=====

This is an alert plugin for the cabot service monitoring tool. It allows you to alert users by Plivo sms.

## Installation

* add PLIVO_AUTH_ID, PLIVO_AUTH_TOKEN, PLIVO_OUTGOING_NUMBER in cabot/conf/development.env
* (on host) vagrant up
* (on guest) copy and run provision
* (on host) vagrant ssh
* (on guest) sudo -H pip install https://github.com/Razvy000/cabot_alert_plivo/archive/master.zip --upgrade
* (on guest) foreman run python manage.py syncdb --migrate
* (on guest) foreman start

* Enter the cabot virtual environment.
* $ pip install cabot-alert-plivo
* $ foreman stop
* Add cabot_alert_plivo to the installed apps in settings.py
* $ foreman run python manage.py syncdb
* $ foreman start