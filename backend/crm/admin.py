from django.contrib import admin
from .models import Call, OrderStatus, Booking, CommentCall, CommentBooking


class CommentBookingInl(admin.StackedInline):
    model = CommentBooking
    fields = ('comment_date', 'comment_text')
    readonly_fields = ('comment_date',)
    extra = 0


class CommentCallInl(admin.StackedInline):
    model = CommentCall
    fields = ('comment_date', 'comment_text')
    readonly_fields = ('comment_date',)
    extra = 0


class BookAdm(admin.ModelAdmin):
    list_display = (
        'id', 'order_status', 'order_name', 'order_date', 'order_phone', 'booking_where', 'booking_quantity',
        'order_comment')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_date')
    list_filter = ('order_status',)
    list_editable = ('order_status',)
    list_per_page = 10
    readonly_fields = ('booking_date',)
    inlines = [CommentBookingInl, ]


class CallAdm(admin.ModelAdmin):
    list_display = (
        'id', 'order_status', 'order_name', 'order_date', 'order_phone', 'order_comment')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_date')
    list_filter = ('order_status',)
    list_editable = ('order_status',)
    list_per_page = 10
    inlines = [CommentCallInl, ]


admin.site.register(Call, CallAdm)
admin.site.register(Booking, BookAdm)
