from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
import datetime
from .models import *
from PIL import Image
from io import StringIO
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email address', error_messages={'exists': 'Oops, this email address already exists.'})
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']

class AddServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = [
            'image',
            'start_city',
            'end_city',
            'start_date',
            'end_date',
            'ask_price',
            'message',
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddServiceForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AddServiceForm, self).save(commit=False)

        if commit:
            instance.save()
        return instance

class AddNeedsForm(forms.ModelForm):

    class Meta:
        model = Need
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

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddNeedsForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AddNeedsForm, self).save(commit=False)

        if commit:
            instance.save()
        return instance

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'msg_content',
            'receiver',
        ]
        widgets = {'receiver': forms.HiddenInput()}
    def save(self, commit=True):
        message = Message()
        message.msg_content = self.cleaned_data['msg_content']
        message.receiver = self.cleaned_data['receiver']

        if commit:
            message.save()
        return message

class replyMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'msg_content',
            'sender',
        ]
        widgets = {'sender': forms.HiddenInput()}
    def save(self, commit=True):
        message = Message()
        message.msg_content = self.cleaned_data['msg_content']
        message.sender = self.cleaned_data['sender']

        if commit:
            message.save()
        return message

