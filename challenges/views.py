from django.shortcuts import render 
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect 
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

#first view
#django will send the request itself


days = {
    'saturday' : 'this is saturday',
    'sunday' : 'this is sunday',
    'monday' : 'this is monday',
    'tuesday' : 'this is tuesday',
    'wednesay' : 'this is wednesday',
    'thursday' : 'this is thursday',
    'friday' : 'this is friday',
}

def deys_list(request):
    days_list = list(days.keys())
    allDays = ""
    for day in days_list:
        url_path = reverse("days-of-week", args = [day])
        allDays += f'<li> <a href = "{url_path}"> {day} </a> </li>\n'
        # now each day would be shown as a link to the path that has a name

    content = f'<ul> {allDays} </ul>'
    
    return HttpResponse(content)



def dynamic_url(request, word):
    response = render_to_string('challenges/challenges.html') # using the template
    return HttpResponse(response + word) # word will be shown under the template



def index_sunday(request):
    return HttpResponse("this is sunday")

def index_monday(request):
    return HttpResponse("this is monday")

def index_wednesday(request):
    return HttpResponse("this is wednesday")



def day_num(request, num):
    allDays = list(days.keys())
    if num > len(days):
        return HttpResponseNotFound('less then 7 pls')
    else:
        day = allDays[num - 1]
        # return HttpResponseRedirect(f'/challenges/{day}') # this will send "http://127.0.0.1:8000/challenges/1" to "http://127.0.0.1:8000/challenges/saturday"
        # what if the prefix suddenly changed in the main app urls? we should make it dynamic
        redirectURL = reverse("days-of-week", args = [day]) # args here just accepts a list that's why we use []
        return HttpResponseRedirect(redirectURL)
        # this the most dynamic it gets so it will work
        # if u change the main url it will send u to the sub url with days-of-week name no matter what is the main url
        # wether it's days-of-week/ or ahhf/ the reverse works 



def dayToName_dynamic(request,day,name):
    day_data = days.get(day)
    if day_data is not None:
        return HttpResponse(f'hi {name}, {day_data}')
    
    return HttpResponseNotFound('day not found')

