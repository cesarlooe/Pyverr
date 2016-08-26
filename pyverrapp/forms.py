from django.forms import ModelForm, Select, Textarea, NumberInput, FileInput, CheckboxInput
from .models import Gig

class GigForm(ModelForm):
    class Meta:
        model = Gig
        fields = ['title', 'category', 'description', 'price', 'photo', 'status']
        widgets = {
            'title': Textarea(attrs={'class':'form-control', 'rows':3}),
            'category': Select(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control', 'rows':5}),
            'price': NumberInput(attrs={'class':'form-control', 'default':6}),
            'photo': FileInput,
        }