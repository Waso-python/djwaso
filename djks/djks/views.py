from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now
    name = 'waso'
    _context = {'date':date, 'name':name}
    return render(request, 'home.html', _context)
