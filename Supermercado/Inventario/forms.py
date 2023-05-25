from django import forms
from .choices import*
from .models import*

class AddProveedorForm(forms.Form):
    rtn = forms.CharField(max_length=14, label='RTN', widget=forms.TextInput(attrs={'class':'form-control'}))
    name = forms.CharField(max_length=150, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(max_length=4, label='Cuidad', widget=forms.Select(attrs={'class':'form-select'}, choices=CITIES))
    address = forms.CharField(max_length=255, label='Direccion', widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=70, label='Correo Electronico', widget=forms.TextInput(attrs={'class':'form-control', 'type':'email'}))
    phone = forms.CharField(max_length=8, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}))
    
class UpdateProveedorFrom(forms.ModelForm):
    rtn = forms.CharField(max_length=14, label='RTN', widget=forms.TextInput(attrs={'class':'form-control'}))
    name = forms.CharField(max_length=150, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(max_length=4, label='Cuidad', widget=forms.Select(attrs={'class':'form-select'}, choices=CITIES))
    address = forms.CharField(max_length=255, label='Direccion', widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=70, label='Correo Electronico', widget=forms.TextInput(attrs={'class':'form-control', 'type':'email'}))
    phone = forms.CharField(max_length=8, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Proveedor
        fields = ['rtn', 'name', 'city','address','email','phone']



class AddProductoForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(label='Precio', widget=forms.NumberInput(attrs={'class':'form-control'}))
    provider = forms.ModelChoiceField(queryset=Proveedor.objects.all(),label='Proveedor', widget=forms.Select(attrs={'class':'form-select'}))

class UpdateProductForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(label='Precio', widget=forms.NumberInput(attrs={'class':'form-control'}))
    provider = forms.ModelChoiceField(queryset=Proveedor.objects.all(),label='Proveedor', widget=forms.Select(attrs={'class':'form-select'}))

    class Meta:
        model = Producto
        fields = ['name', 'price', 'provider']
