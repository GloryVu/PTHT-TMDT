from django import forms
from eos.models import Author
 
class AuthorForm(forms.ModelForm):
 
    class Meta:
        model = Author
        fields = [
            "name",
            "biography",
        ]