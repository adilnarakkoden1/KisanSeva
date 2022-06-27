from django import forms
from django.contrib.auth.forms import UserCreationForm

from seva_app.models import Login, notification, market


class DateInput(forms.DateInput):
    input_type = 'date'


class Officerform(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username','password1','password2','name', 'email', 'address', 'gender', 'contact_no', 'location')


class Techinicalform(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username','password1','password2','name', 'email', 'address', 'contact_no', 'location')
class farmerform(UserCreationForm):
    class Meta:
        model= Login
        fields = ('username', 'password1', 'password2', 'name', 'address', 'contact_no','specialisation')



class notificationForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = notification
        fields = ('date', 'subject', 'description')

class marketForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = market
        fields = ('name', 'type', 'quantity','location', 'phone', 'amount')


# class sendnotificationForm(forms.ModelForm):
#     date = forms.FileField(widget=DateInput)
#     class Meta:
#         model = market
#         fields = ('name')
