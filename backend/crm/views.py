from django.shortcuts import render
from .models import Call, Booking
from telebot.sendmessage import send_telegram_call, send_telegram_booking

import re


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def fleet(request):
    return render(request, 'fleet.html')


def contacts(request):
    return render(request, 'contacts.html')


def card(request):
    return render(request, 'card.html')


def thanks_page_call(request):
    if request.POST:
        name = request.POST["name"]
        if len(name) < 2 or re.search('\d+', name):
            return render(request, 'error.html', context={'error': 'Имя'})
        phone = request.POST["phone"]
        print(len(phone))
        if len(phone) < 11:
            return render(request, 'error.html', context={'error': 'Телефон'})
        comment = request.POST["comment"]
        new_call = Call(order_name=name, order_phone=phone, order_comment=comment)
        new_call.save()
        send_telegram_call(name, phone, comment)
        return render(request, 'thanks.html')


def thanks_page_booking(request):
    if request.POST:
        name = request.POST["name"]
        if len(name) < 2 or re.search('\d+', name):
            return render(request, 'error.html', context={'error': 'Имя'})
        phone = request.POST["phone"]
        if len(phone) < 11:
            return render(request, 'error.html', context={'error': 'Телефон'})
        comment = request.POST["comment"]
        where = request.POST["where"]
        date = request.POST["date"]
        quantity = request.POST["quantity"]
        new_booking = Booking(order_name=name, order_phone=phone, order_comment=comment,
                              booking_where=where,
                              booking_date=date, booking_quantity=quantity)
        new_booking.save()
        send_telegram_booking(name, phone, comment, where, date, quantity)
        return render(request, 'thanks.html')
