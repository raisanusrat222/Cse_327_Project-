from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class RegForm(UserCreationForm):
    """
        This class is used to create the premium member and employee registration page.

        :param request: it's a form request from user.
    """
   
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter User Name"}))
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def clean_username(self):
        username = self.cleaned_data['username']

        for instance in User.objects.all():
            if instance.username == username:
                raise forms.ValidationError('this user name:  (' + username + ')  already exists' )
        return username        


