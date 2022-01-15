from .models import User
from django.contrib.auth.forms import UserCreationForm# , UserChangeForm <--- If we have time

class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = User
        fields = ('email,first_name,last_name,location,current_classes,previous_classes')

