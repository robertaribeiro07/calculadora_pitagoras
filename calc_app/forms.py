from django import forms

class MeuForm(forms.Form):
  cat1 = forms.CharField(max_length=255)
  cat2 = forms.CharField(max_length=255)