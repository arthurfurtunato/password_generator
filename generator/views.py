from django.shortcuts import render
import string, random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def generator(request):
    return render(request, 'generator.html', {
        'range': range(6, 15),
    })

def password(request):
    length = request.POST.get('length')
    password1 = ''
    password2 = ''
    password3 = ''
    if 'uppercase' in request.POST:
        password1 = string.ascii_uppercase

    if 'special' in request.POST:
        password2 = string.punctuation

    if 'numbers' in request.POST:
        password3 = string.digits
    
    password = ''.join(random.choice(string.ascii_lowercase + password1 + password2 + password3) for i in range(int(length)))

    return render(request, 'password.html',{
        'password': password,
    })