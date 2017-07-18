
# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View, TemplateView, CreateView
from catalog.models import Category
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

#def index(request):

 #   return render(request, 'index.html')

class IndexView(TemplateView):

    template_name = 'index.html'

# o método as_view transforma a classe em um objeto chamável
index = IndexView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)

def product_list(request):
    return render(request, 'product_list.html')


def product(request):
    return render(request, 'product.html')

User = get_user_model()
