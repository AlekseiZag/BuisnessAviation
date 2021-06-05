from django import forms


class BookingForm(forms.Form):
    booking_where = forms.CharField(max_length=200, required=False)
    booking_date = forms.DateField(required=False)
    booking_quantity = forms.IntegerField(required=False)
    order_name = forms.CharField(max_length=200)
    order_phone = forms.CharField(max_length=200)
    order_comment = forms.CharField(max_length=200, required=False)
