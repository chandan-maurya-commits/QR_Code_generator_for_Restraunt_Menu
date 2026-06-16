from django import forms


class QRCodeForm(forms.Form):
    restraunt_name = forms.CharField(
        max_length=50, 
        label='Restraunt Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Restraunt Name',
        })
        
        )
    url = forms.URLField(
        max_length=200, 
        label='Menu URL',
        widget=forms.URLInput(attrs={
            'class':'form-control',
            'placeholder':'Enter the URL of your online menu',
        }))