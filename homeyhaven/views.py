from django.shortcuts import render
from hotels.models import Hotel

def home(request):
    hotel = Hotel.objects.all()
    return render(request, 'index.html', {'hotels' : hotel})