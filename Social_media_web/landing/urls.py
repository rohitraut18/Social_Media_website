from django.urls import path
from landing.views import Index
from landing.views import About

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
]
