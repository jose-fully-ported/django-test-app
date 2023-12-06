from django.http import HttpResponse
from django_redis import get_redis_connection


def index(request):
    conn = get_redis_connection("default")
    return HttpResponse(f"Hello, world. You're at the polls index: {conn.ping()}")
