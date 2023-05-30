import time

from django.http import HttpRequest
from django.shortcuts import render


def setup_useragent_on_request_middleware(get_response):
    print('Initial call')

    def middleware(request: HttpRequest):
        print('before get response')
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        print('after get response')
        return response

    return middleware


class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print('requests_count', self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print('responses_count', self.responses_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print('got', self.exceptions_count, 'exceptions so far')


class ThrottlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_time = {}
        self.last_request_datatime = 0

    def __call__(self, request: HttpRequest):
        if request.method == 'GET':
            timing = 3
            if not self.request_time:
                print('First request')
            else:
                if time.time() - self.request_time['time'] < timing \
                        and self.request_time['ip_address'] == request.META.get('REMOTE_ADDR'):
                    return render(request, 'requestdataapp/error-time-request.html')

            self.request_time = {'time': time.time(), 'ip_address': request.META.get('REMOTE_ADDR')}
        response = self.get_response(request)

        return response
