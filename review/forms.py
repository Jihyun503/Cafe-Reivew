from django import forms
from .models import *
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

class ReviewForm(forms.ModelForm):
    shop_name = forms.CharField(
        label="상호명",
        required=True,
        widget=forms.TextInput(
            attrs={
                "id" : "shop_name",
                "class" : "form-control",
            }
        ),
    )

    address = forms.CharField(
        label="주소",
        required=True,
        widget=forms.TextInput(
            attrs={
                "id" : "address",
                "class" : "form-control",
            }
        ),
    )

    contents = SummernoteTextField()

    '''
    contents = forms.CharField(
        label="내용",
        required=True,
        widget=forms.Textarea(
            attrs={
                "id" : "contents",
                "class" : "form-control",
            }
        )
    )
    '''
    class Meta:
        model = Review
        widgets = {
            'contents' : SummernoteWidget(),
        }
        fields = ['shop_name', 'address', 'contents']


    