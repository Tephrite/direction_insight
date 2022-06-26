from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def what_we_do(request):
    return render(request, 'what_we_do.html')

def reviews(request):
    return render(request, 'reviews.html')