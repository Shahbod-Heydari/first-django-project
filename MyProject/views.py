# i made this for the main front page, as u know, for every page of any apps, u should make the views for it seperatly

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("this is the main front page")