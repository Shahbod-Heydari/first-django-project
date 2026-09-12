# we made this file ourselves
from django.urls import path
from . import views # . means this folder

urlpatterns = [
    path('',views.days_list),
    path('sunday', views.index_sunday),# no () so we don't have to send request, we just write refrence and it sends request itself
    # it will connect the sunday address to the index function
    path('monday', views.index_monday),
    path('wednesday', views.index_wednesday),
    path('<int:num>', views.day_num),
    path('days', views.all_days),
    path('<word>', views.dynamic_url, name='days-of-week'), # this a dynamic url meaning everything after challenges/ would land here exept the 3 days we determined seperately
    # using anything other than word here would not work because we used word in the view method
    path('<int:num>/<name>', views.day_and_name_dyanmic),
    path('<day>/<name>', views.dayToName_dynamic) # now "http://127.0.0.1:8000/challenges/tuesday/sjhki" shows "hi sjhki, this is tuesday"
]
# now we should introduce these urls in the urls in the main app