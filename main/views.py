from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406453392',
        'name': 'Arisa Rae',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)