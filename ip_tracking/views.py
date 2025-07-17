from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from ratelimit.decorators import ratelimit

# Create your views here.

# Sensitive login view with rate limiting
@ratelimit(key='ip', rate='10/m', method='POST', block=True)
@ratelimit(key='ip', rate='5/m', method='POST', block=True, group='anon', condition=lambda r: not r.user.is_authenticated)
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login successful')
        else:
            return HttpResponse('Invalid credentials', status=401)
    return render(request, 'login.html')
