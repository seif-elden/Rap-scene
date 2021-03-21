from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


from .models import community_post , comments


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())

    class Meta:
        model=User
        fields = {'first_name','last_name','email','username','password1','password2'}

    field_order = ['first_name','last_name','email','username','password1','password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class f_community_post(forms.ModelForm):
    class Meta :
        model = community_post
        fields = ('image','caption')
        widgets = {
            "caption":forms.Textarea(attrs={"rows":5}),
            }


    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get("caption") and not cleaned_data.get("image") :
            raise ValidationError({"caption":"the post cannot be empty","image":"the post cannot be empty"})

 

class f_comments(forms.ModelForm):
    class Meta :
        model = comments
        fields = ('comment',)