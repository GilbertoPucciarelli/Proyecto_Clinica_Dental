
from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class SignUpForm(forms.Form):

    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    email = forms.CharField(widget=forms.EmailInput())

    
    def cleaned_username(self):

        username = self.cleaned_data['username']
        query = User.objects.filter(username=username).exists()

        if query:

            raise forms.ValidationError('User Name is already in use')

        return username


    def clean(self):

        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:

            raise forms.ValidationError('Passwords do not match')

        return data


    def save(self):

        data = self.cleaned_data
        data.pop('password_confirmation')
        
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class EditUserForm(forms.ModelForm):

    class Meta:
        
        model = Profile
        fields = ('bloqued', 'role',)