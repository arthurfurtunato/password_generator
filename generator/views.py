from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'range': range(1, 11),
    })

def password(request):
    return render(request, 'password.html')