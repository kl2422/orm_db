from django.shortcuts import render
from django.views.decorators.http import require_http_methods

# Create your views here.


def page_not_found_view(request):
    print(404)
    return render(request, "404.html")


def permission_denied_view(request):
    print(403)
    return render(request, "403.html")


def server_error_view(request):
    print(500)
    return render(request, "500.html")



