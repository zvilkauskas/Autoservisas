from .models import OrderListReview, Profile
from django import forms
from django.contrib.auth.models import User


class OrderListReviewForm(forms.ModelForm):
    class Meta:
        model = OrderListReview
        fields = ('content', 'order_list', 'reviewer',)
        widgets = {'order_list': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
