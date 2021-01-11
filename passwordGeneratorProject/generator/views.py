from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/index.html')


def password(request):
    char = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length'))
    password = ''

    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        char.extend(list('1234567890'))
    if request.GET.get('specialChar'):
        char.extend(list('~!@#$%^&*()_+=-`'))

    for i in range(length):
        password += random.choice(char)

    return render(request, 'generator/password.html', {'password':password})


def about(request):
    return render(request, 'generator/about.html')