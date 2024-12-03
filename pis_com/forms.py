from django import forms
from pis_com.models import Customer, FeedBack
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label="Email"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'


