from django.shortcuts import render


# Create your views here.

posts = [
    {
        'author':'AAA',
        'title':'one',
    }
]

def conf_choose(request):
    context = {
        'posts': posts
    }
    return render(request, 'settings_config/conf_choose.html', context)

def devices(request):
    context = {

    }
    return render(request, 'settings_config/devices.html', context)

def loading():
    return

def installed(request):
    context ={

    }
    return render(request, 'settings_config/installed.html', context)

def finish():
    return

