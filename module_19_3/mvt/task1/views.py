from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
from .models import *

# Create your views here.

# users = ['Alex', 'Max']
users = []

buyers = Buyer.objects.all()
for buyer in buyers:
    users.append(buyer.name)
print(users)


def shop_games_task4(request):
    return render(request, 'shop_game_task4.html')

def games_task4(request):
    # games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    # context = {
    #     'games': games,
    # }
    #
    # return render(request, 'games_task4.html', context)

    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'games_task4.html', context)

def cart_task4(request):
    status = 'Извините, ваша корзина пуста'
    context = {
        'status': status,
    }
    return render(request, 'cart_task4.html', context)



def registration_page(request):
    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            if username in users:
                info['error'] = 'Пользователь уже существует!'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают!'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18 лет!'
            else:
                Buyer.objects.create(name=username, balance=1000, age=age)
                return HttpResponse(f'Приветствуем, {username}! (Django)')
            return HttpResponse(f'Ошибка регистрации: {info["error"]} (Django)')
        else:
            info['form'] = form
    else:
        form = UserRegister()
        info['form'] = form
    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            print(info)
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
            print(info)
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            print(info)
        else:
            return HttpResponse(f'Приветствуем, {username}! (HTML)')
        return HttpResponse(f'Ошибка регистрации: {info["error"]} (HTML)')

    return render(request, 'registration_page.html', info)
