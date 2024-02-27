from django.shortcuts import render
from web.models import Practice

def index(request):
    practices = Practice.objects.all()
    
    context = {
        "practices": practices
        

    }
    return render(request, 'index.html')
