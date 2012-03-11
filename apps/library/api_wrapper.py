from apps.library import ZenLib

class ApiWrapper(ZenLib):
    """A wrapper to make user api calls                                                                                                             
    """

    def ticket_info(self, page=None):
        data = {'page':page} if page else {}
        return self._make_request('ticket-info', data, method='GET')

    def ticket_detail(self, ticket_id):
        return self._make_request('ticket-detail', {}, ticket_id, 'GET')
