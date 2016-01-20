from os import environ as env

from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template import Context, Template

from cabot.cabotapp.alert import AlertPlugin

import requests
import logging

import plivo

# get the environment variables (see cabot/conf/development.env)
auth_id = env.get('PLIVO_AUTH_ID')
auth_token = env.get('PLIVO_AUTH_TOKEN')
plivoClient = plivo.RestAPI(auth_id, auth_token)

plivo_template = "Service {{ service.name }} {% if service.overall_status == service.PASSING_STATUS %}is back to normal{% else %}reporting {{ service.overall_status }} status{% endif %}: {{ scheme }}://{{ host }}{% url 'service' pk=service.id %}. {% if service.overall_status != service.PASSING_STATUS %}Checks failing: {% for check in service.all_failing_checks %}{% if check.check_category == 'Jenkins check' %}{% if check.last_result.error %} {{ check.name }} ({{ check.last_result.error|safe }}) {{jenkins_api}}job/{{ check.name }}/{{ check.last_result.job_number }}/console{% else %} {{ check.name }} {{jenkins_api}}/job/{{ check.name }}/{{check.last_result.job_number}}/console {% endif %}{% else %} {{ check.name }} {% if check.last_result.error %} ({{ check.last_result.error|safe }}){% endif %}{% endif %}{% endfor %}{% endif %}{% if alert %}{% for alias in users %} @{{ alias }}{% endfor %}{% endif %}Raz"


class PlivoAlert(AlertPlugin):
	name = "Plivo SMS"
	author = "Razvan Pistolea"

	def send_alert(self, service, users, duty_officers):

		c = Context({
            'service': service,
            'host': settings.WWW_HTTP_HOST,
            'scheme': settings.WWW_SCHEME
        })
		t = Template(plivo_template)
		msg = t.render(c)
		send_response = plivoClient.Message.send(
			src='441233801333',
			dst='447482254604',
			text=msg,
			url='http://localhost.com',
		)