from datetime import datetime

from django import template

from django.contrib.humanize.templatetags import humanize

register = template.Library()

@register.filter
def time_since(value):
    value_datetime = datetime.strptime(value,"%Y-%m-%dT%H:%M:%SZ")
    return humanize.naturaltime(value_datetime)
