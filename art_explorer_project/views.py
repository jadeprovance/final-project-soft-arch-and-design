
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def home(request):
    
    context = {
        'message': 'Welcome to Art Explorer!',
    }

    return render(request, 'home.html', context)
