from django import forms

# Cria a classe de formulário
class MeuForm(forms.Form):
  cat1 = forms.CharField(max_length=255)
  cat2 = forms.CharField(max_length=255)
