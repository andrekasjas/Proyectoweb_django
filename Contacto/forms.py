from django import forms

class Formulario_contacto(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contenido = forms.CharField(label="Contenido", required=True, widget=forms.Textarea)
