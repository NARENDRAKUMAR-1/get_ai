from django.shortcuts import render, HttpResponse

# Create your views here.


def home1(request):
    return render(request, 'home1.html')
