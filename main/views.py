from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Kelvin Saputra',
        'class': 'PBP F',
        'NPM'  : 2206027186
    }

    return render(request, "main.html", context)