import simplejson as json

from django.conf import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404, HttpResponseRedirect, \
    HttpResponse

from apps.library.api_wrapper import ApiWrapper

LIB_OBJ = ApiWrapper()

TICKET_STATUS = {'0':'New', '1':'Open', '2':'Pending', '3':'Solved', '4':'Closed'}

def get_tickets(request, page=None, status_id=None):
    context = RequestContext(request)
    tickets = LIB_OBJ.ticket_info(page)
    ticket_obj = [{'subject':ticket.get('subject'), 'description':ticket.get('description'), \
                       'created_at':ticket.get('created_at').split(' ')[0], \
                       'year':ticket.get('created_at').split(' ')[0].split('/')[0], \
                       'month':'%s/%s' % (ticket.get('created_at').split(' ')[0].split('/')[0],\
                                              ticket.get('created_at').split(' ')[0].split('/')[1]),
                       'status':TICKET_STATUS.get(str(ticket.get('status_id'))),\
                       'ticket_id':ticket.get('nice_id')} \
                      for ticket in tickets]
    if status_id:
        ticket_obj = [obj for obj in ticket_obj if obj.get('status') == TICKET_STATUS.get(status_id)]
        group = request.GET.get('group')
        if group:
            context['group'] = group
        context['status_id'] = status_id

    context['tickets'] = ticket_obj
    return render_to_response('index.html', context_instance=context)
    #return HttpResponse(json.dumps({'ticket_info':ticket_obj}), mimetype='application/javascript')
    
def ticket_detail(request, ticket_id):
    context = RequestContext(request)
    ticket_obj = LIB_OBJ.ticket_detail(ticket_id)
    context['ticket_obj'] = ticket_obj
    return render_to_response('detail.html', context_instance=context)
