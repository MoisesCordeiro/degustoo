from django import forms

from degAuth.models import Usuario
from django.forms import ModelForm

class Form_Registro(ModelForm):

    nome = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control'}))
    sobrenome = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    telefone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    senha1 = forms.CharField(min_length=6, max_length=12, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    senha2 = forms.CharField(min_length=6, max_length=12, widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = Usuario
        fields = ['email', 'telefone']
    
    def clean_senha2(self):
        pass1 = self.cleaned_data['senha1']
        pass2 = self.cleaned_data['senha2']
        
        if (pass1 and pass2) and (pass1 == pass2):
            return pass2
        else:
            raise forms.ValidationError("Passwords do not match")

class Form_Login(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label="Senha")