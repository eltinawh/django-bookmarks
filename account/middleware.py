from django.shortcuts import redirect
from django.urls import reverse


class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        login_url = reverse("login")
        if request.path == login_url and request.user.is_authenticated:
            return redirect("dashboard")
        return self.get_response(request)