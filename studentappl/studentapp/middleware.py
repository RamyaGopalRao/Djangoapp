# studentapp/middleware.py

from django.shortcuts import redirect

class EnsureAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path.startswith('/accounts/'):
            return redirect('login')

        response = self.get_response(request)
        return response
