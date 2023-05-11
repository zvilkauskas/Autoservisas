from .models import OrderListReview
from django import forms

class OrderListReviewForm(forms.ModelForm):
    class Meta:
        model = OrderListReview
        fields = ('content', 'order_list', 'reviewer',)
        widgets = {'order_list': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}