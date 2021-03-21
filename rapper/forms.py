from django import forms
from .models import ad 


class f_ad(forms.ModelForm):
    class Meta :
        model = ad
        fields = "__all__"

        widgets = {
            "msg":forms.Textarea(attrs={"class":"form-control","placeholder":"Your msg *","style":"width: 100%; height: 150px;"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Your email *"}),
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Your Name *"}),
            "phone":forms.TextInput(attrs={"class":"form-control","placeholder":"Your phone *"}),
            }
