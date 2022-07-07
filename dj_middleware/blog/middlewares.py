
# *************Function based middleware*************

"""
def my_middleware(get_response):
    print('One time Function based middleware Initialization')

    def my_function(request):
        print('this is before view Function based')
        # Write code here for run before view...
        response = get_response(request)
        print('This is after view Function based')
        # Write code here for run after view...
        return response
    return my_function
"""

# *************Class based middleware*************

"""
class myMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('One time Class based middleware Initialization')

    def __call__(self, request):
        print('this is before view Class based')
        response = self.get_response(request)
        print('This is after view Class based')

        return response
"""


# *************Class based middleware more then one*************


from django.http import HttpResponse

"""
class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('One time Class based middleware Initialization ``` BrotherMiddleware')

    def __call__(self, request):
        print('this is before Brother view Class based')
        response = self.get_response(request)
        print('This is after Brother view Class based')

        return response

class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('One time Class based middleware Initialization ``` FatherMiddleware')

    def __call__(self, request):
        print('this is before Father view Class based')
        # response = self.get_response(request) # Send next middleware
        response = HttpResponse('Nikl lo') # Not send next middleware, return back from here
        print('This is after Father view Class based')

        return response


class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('One time Class based middleware Initialization ``` MotherMiddleware')

    def __call__(self, request):
        print('this is before Mother view Class based')
        response = self.get_response(request)
        print('This is after Mother view Class based')

        return response
"""


# *************Process Middleware*************
"""
class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(request, *args, **kwargs):
        print('This is Process View - Before View')
        # return HttpResponse('This is before view!!')
        return None
"""

# *************Exception Middleware*************

"""
class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print('Exception Occured')
        msg = exception
        return HttpResponse(msg)
"""

# *************Template Response Middleware*************

class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print('Process Template Response From Middleware')
        response.context_data['name'] = 'Hacker Udoy'
        return response