from django.urls import re_path

from .views import BookListAPI

app_name = 'books'
urlpatterns = [
    re_path(r'^v1/book/', BookListAPI.as_view({
        'get': 'list'
    }), name='bookings-list'),
]