from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import math
from .forms import MeuForm

def hipotenusa(request):
  form = MeuForm(request.POST or None)
  hipotenusa = '??????'
  if form.is_valid():
      cat1 = int(form.cleaned_data['cat1'])
      cat2 = int(form.cleaned_data['cat2'])
      print(cat1, cat2)
      somacatetos = (cat1 * cat1) + (cat2 * cat2)
      hipotenusa = math.sqrt(somacatetos)
    
  return render(request, 'pitagoras.html', {'form': form, 'hipotenusa': hipotenusa})