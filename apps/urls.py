from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apps.views',
    url(r'^$', 'get_tickets', name='get_tickets'),  
    url(r'status/(?P<status_id>.+)/$', 'get_tickets', name='get_tickets_status'),  
    url(r'tickets/(?P<ticket_id>.+)/$', 'ticket_detail', name='ticket_detail'),  
    url(r'(?P<page>.+)/$', 'get_tickets', name='get_tickets_page'),  
)
