from django.shortcuts import render, redirect
from random import randint
from datetime import datetime


def index(request):
    if 'total_gold' not in request.session or 'activities' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')


def process_money(request):
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            gold = randint(10, 20)
            request.session['activities'].append('You are earned ' + str(gold) + ' golds from the ' +

                                                 request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['building'] == 'cave':
            gold = randint(5, 10)
            request.session['activities'].append('You are earned ' + str(gold) + ' golds from the ' +
                                                 request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['building'] == 'house':
            gold = randint(2, 5)
            request.session['activities'].append('You are earned ' + str(gold) + ' golds from the ' +
                                                 request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['building'] == 'casino':
            gold = randint(-50, 50)
            if gold >= 0:
                request.session['activities'].append('Entered a casino and earned ' + str(
                    gold) + ' gold' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
            else:
                request.session['activities'].append('Entered a casino and lost ' + str(
                    gold) + ' gold... Ouch...' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        request.session['total_gold'] += gold

    return redirect('/')


def reset(request):
    if request.method == "POST":
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return redirect('/')
