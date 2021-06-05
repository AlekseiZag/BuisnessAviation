from django.db import models


class OrderStatus(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=20, verbose_name='Телефон')
    order_comment = models.CharField(max_length=200, verbose_name='Комментарий пользователя')
    order_status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, null=True, blank=True,
                                     verbose_name='Статус')

    def __str__(self):
        return self.order_name


class Call(Order):
    class Meta:
        verbose_name = 'Заявка на зонок'
        verbose_name_plural = 'Заявки на звонок'


class Booking(Order):
    booking_where = models.CharField(max_length=200, verbose_name='Куда')
    booking_date = models.CharField(max_length=50, verbose_name='Дата поездки')
    booking_quantity = models.CharField(max_length=200, verbose_name='Количество пассажиров')

    class Meta:
        verbose_name = 'Заявка на бронирование'
        verbose_name_plural = 'Заявки на бронирование'


class Comment(models.Model):
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class CommentCall(Comment):
    comment_binding = models.ForeignKey(Call, on_delete=models.CASCADE, verbose_name='Заявка')

    class Meta:
        verbose_name = 'Комментарий (звонки)'
        verbose_name_plural = 'Комментарии (звонки)'


class CommentBooking(Comment):
    comment_binding = models.ForeignKey(Booking, on_delete=models.CASCADE, verbose_name='Заявка')

    class Meta:
        verbose_name = 'Комментарий (бронь)'
        verbose_name_plural = 'Комментарии (бронь)'
