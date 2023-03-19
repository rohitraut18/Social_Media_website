from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/about.html')

