from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Create your views here.
def what_we_do(request):
    return render(request, 'what_we_do.html')