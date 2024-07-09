from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('hi')

def log(request):
    return render(request, 'log.html')
    #return HttpResponse('log hi')

def log1(request):
    return render(request, 'log1.html')

def log2(request):
    return render(request, 'log2.html')

def signup1(request):
    return render(request, 'signup1.html')

def signup2(request):
    return render(request, 'signup2.html')

def result1(request):
    return render(request, 'result1.html')

def result2(request):
    return render(request, 'result2.html')