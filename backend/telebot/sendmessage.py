import requests
from .models import TeleSettings


def send_telegram_call(tg_name, tg_phone, tg_comment):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = settings.tg_token
        chat_id = settings.tg_chat_id
        text = settings.tg_message
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'
        if text:
            text = text[:66]
            part_1 = text[:20] + tg_name + text[26]
            part_2 = text[27:36] + tg_phone + text[43]
            part_3 = text[44:57] + tg_comment
            full_text = part_1 + part_2 + part_3
        else:
            full_text = tg_name + ' ' + tg_phone + ' ' + tg_comment
        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': full_text
            })
        except:
            pass
        finally:
            if req.status_code == 200:
                print('Cooбщение отправлено')
            else:
                print('Ошибка отправки')
    else:
        pass


def send_telegram_booking(tg_name, tg_phone, tg_comment, tg_where, tg_date, tg_quantity):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = settings.tg_token
        chat_id = settings.tg_chat_id
        text = settings.tg_message
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'
        if text:
            part_1 = text[:20] + tg_name + text[26]
            part_2 = text[27:36] + tg_phone + text[43]
            part_3 = text[44:57] + tg_comment + text[66]
            part_4 = text[67:73] + tg_where + text[80]
            part_5 = text[81:87] + tg_date + text[93]
            part_6 = text[94:117] + tg_quantity
            full_text = part_1 + part_2 + part_3 + part_4 + part_5 + part_6
        else:
            full_text = tg_name + ' ' + tg_phone + ' ' + tg_comment + ' ' + tg_where + ' ' + tg_date + ' ' + tg_quantity
        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': full_text
            })
        except:
            pass
        finally:
            if req.status_code == 200:
                print('Cooбщение отправлено')
            else:
                print('Ошибка отправки')
    else:
        pass
