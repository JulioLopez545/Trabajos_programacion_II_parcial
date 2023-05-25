from django import forms
from .models import*

class AddcargoForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre del cargo', widget=forms.TextInput(attrs={'class':'form-control'}))



class UpdateCargoForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Nombre Del Cargo', widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = Cargo
        fields = ['name']


class AddclienteForm(forms.Form):
    person =  forms.ModelChoiceField(queryset=Persona.objects.all(),label='Cliente', widget=forms.Select(attrs={'class':'form-select'}))
    address = forms.CharField(max_length=255, label='Direccion', widget=forms.Textarea(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=8, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}))

class UpdateclienteForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Persona.objects.all(),label='Cliente', widget=forms.Select(attrs={'class':'form-select'}))
    address = forms.CharField(max_length=255, label='Direccion', widget=forms.Textarea(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=8, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}))

    

    class Meta:
        model = Cliente
        fields = ['person','address','phone']

class AddUsuariosForm(forms.Form):
    person =  forms.ModelChoiceField(queryset=Persona.objects.all(),label='Persona', widget=forms.Select(attrs={'class':'form-select'}))
    position =forms.ModelChoiceField(queryset=Cargo.objects.all(), label='Cargo',widget=forms.Select(attrs={'class':'form-select'}))
    email = forms.CharField(max_length=70, label='Correo Electronico', widget=forms.TextInput(attrs={'class':'form-control', 'type':'email'}))
    phone = forms.CharField(max_length=8, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}))

class UpdateUsuariosForm(forms.ModelForm):
    person =  forms.ModelChoiceField(queryset=Persona.objects.all(),label='Persona', widget=forms.Select(attrs={'class':'form-select'}))
    position =forms.ModelChoiceField(queryset=Cargo.objects.all(), label='Cargo',widget=forms.Select(attrs={'class':'form-select'}))
    email = forms.CharField(max_length=70, label='Correo Electronico', widget=forms.TextInput(attrs={'class':'form-control', 'type':'email'}))
    phone = forms.CharField(max_length=8, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}))

    

    class Meta:
        model = Usuario
        fields = ['person','position','email','phone']