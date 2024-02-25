from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    
    return render(request, "q8/index.html", {
        "is_Kuwaiti_national_day":  now.month == 2 and now.day == 25
    })