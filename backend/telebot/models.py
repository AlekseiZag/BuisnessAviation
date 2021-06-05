from django.db import models


class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat_id = models.CharField(max_length=200, verbose_name='id чата')
    tg_message = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.tg_chat_id

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
