from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'apps_name' : 'Concert Ticket Inventory',
        'name': 'Kelvin Saputra',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)