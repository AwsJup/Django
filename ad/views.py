from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class AboutPageView(TemplateView):
    template_name = 'about.html'
