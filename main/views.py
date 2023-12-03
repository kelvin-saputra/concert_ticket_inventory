import json
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect
from main.forms import ItemForm
from main.models import Item
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.serializers import serialize
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import datetime

@login_required(login_url='/login')
def show_main(request):
    tickets = Item.objects.filter(user=request.user)
    ticket_count = len(tickets)
    context = {
        'name': request.user.username,
        'tickets': tickets,
        'count' : ticket_count,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main")) 
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        else:
            messages.info(request, 'Incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_amount(request, id):
    data = Item.objects.filter(user=request.user).get(pk=id)
    data.amount +=1
    data.save(update_fields=['amount'])
    return redirect('main:show_main')

def min_amount(request, id):
    data = Item.objects.filter(user=request.user).get(pk=id)
    response = redirect('main:show_main')

    if data.amount == 0:
        return response

    data.amount -= 1
    data.save(update_fields=['amount'])
    return response

def delete_data(request, id):
    data = Item.objects.filter(user=request.user).filter(pk=id)
    data.delete()
    return redirect('main:show_main')

def edit_data(request, id):
    data = Item.objects.get(pk = id)
    form = ItemForm(request.POST or None, instance=data)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_data.html", context)

def get_item_json(request):
    item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_item(request, id):
    item = Item.objects.filter(user=request.user).get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def get_user_item(request):
    user = request.user

    if user.is_authenticated:
        user_id = user.id
        data = Item.objects.filter(user_id=user_id)
    else:
        data = []
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)