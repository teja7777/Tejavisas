from django import forms
from visas.models import contact
class contact_form(forms.ModelForm):
    email=forms.EmailField(required=True)
    subject=forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    message=forms.CharField(widget=forms.Textarea,)
    #category=forms.CharField(choices=[('question','Question'),('other','other')])
    class Meta():
        model= contact
        fields=['email','subject','message']