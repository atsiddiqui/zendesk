from django.conf import settings
from django.template import Library

register = Library()

PRIORITES = {'0': 'No Priority Set', '1':'Low', '2':'Normal', '3':'High', '4':'Urgent'}

@register.filter
def get_priority(priority_id):
    return PRIORITES.get(priority_id)
