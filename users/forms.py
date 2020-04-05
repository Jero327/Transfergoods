from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.forms import ModelForm
import datetime
from .models import AddNeeds, AddService
from PIL import Image

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

class AddServiceForm(forms.ModelForm):

    class Meta:
        model = AddService
        fields = [
            'start_city',
            'end_city',
            'start_date',
            'end_date',
            'ask_price',
            'message',
        ]

    def save(self, commit=True):
        service = AddService()
        service.start_city = self.cleaned_data['start_city']
        service.end_city = self.cleaned_data['end_city']
        service.start_date = self.cleaned_data['start_date']
        service.end_date = self.cleaned_data['end_date']
        service.ask_price = self.cleaned_data['ask_price']
        service.message = self.cleaned_data['message']
        if commit:
            service.save()
        return service

class AddNeedsForm(forms.ModelForm):

    class Meta:
        model = AddNeeds
        fields = [
            'image',
            'start_city',
            'end_city',
            'start_date',
            'end_date',
            'good_name',
            'offer_price',
            'message',
        ]
    def save(self, commit=True):
        needs = AddNeeds()
        needs.image = self.cleaned_data['image']
        needs.start_city = self.cleaned_data['start_city']
        needs.end_city = self.cleaned_data['end_city']
        needs.start_date = self.cleaned_data['start_date']
        needs.end_date = self.cleaned_data['end_date']
        needs.good_name = self.cleaned_data['good_name']
        needs.offer_price = self.cleaned_data['offer_price']
        needs.message = self.cleaned_data['message']
        if commit:
            needs.save()
        return needs

