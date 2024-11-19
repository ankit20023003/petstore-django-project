from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
    

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        #fields='__all__'
    