from .models import User
from ClassCodes.models import ClassCode
from django.contrib.auth.forms import UserCreationForm# , UserChangeForm <--- If we have time
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','location','current_classes','previous_classes')

class AddClassesForm(forms.Form):
    classes = []
    for e in ClassCode.objects.all().distinct():
        classes.append((e.ClassName, e.ClassName))

    Class= forms.ChoiceField( 
        required = True,
        widget=forms.Select,
        choices=classes)