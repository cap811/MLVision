from django.shortcuts import render

def index(request):
    page_title = 'MLVision – Index'
    return render(request, 'core/index.html', {
        'page_title' : page_title
        })

def stats(request):
    page_title = 'MLVision – Statistics'
    return render(request, 'stats/index.html', {
        'page_title' : page_title
        })

