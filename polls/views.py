from django.core.cache import cache
from django.http import HttpResponse


def index(request):
    return HttpResponse(f"Hello, world. You're at the polls index: {cache.ping()}")
