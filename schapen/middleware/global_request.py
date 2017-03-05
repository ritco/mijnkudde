# coding: utf-8
from threading import current_thread

_requests = {}


def get_request():
    return _requests.get(current_thread())


# Defining own middleware classes was changed in django 1.10
# https://docs.djangoproject.com/en/1.10/topics/http/middleware/
class GlobalRequestMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _requests[current_thread()] = request
        return self.get_response(request)
