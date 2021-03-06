from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
    
        self.fields['username'].widget.attrs = {
            'class': 'form-control',
            'placeholder': ''
        }

        self.fields['email'].widget.attrs = {
            'class': 'form-control',
            'placeholder': ''
        }

        self.fields['first_name'].widget.attrs = {
            'class': 'form-control',
            'placeholder': ' Name'
        }

        self.fields['last_name'].widget.attrs = {
            'class': 'form-control',
            'placeholder': ' Name'
        }

        self.fields['password1'].widget.attrs = {
            'class': 'form-control',
            'placeholder': ''
        }

        self.fields['password2'].widget.attrs = {
            'class': 'form-control',
            'placeholder': ''
        }

        # to remove field
        # del self.fields['username']

    class Meta:
        model = User
        fields = ['username', 'first_name',  'last_name', 'email', 'password1', 'password2']
        
        labels = {
            'username': ('User Name'),
        }


