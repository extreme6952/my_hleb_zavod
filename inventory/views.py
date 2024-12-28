from .models import *
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateResponseMixin,View
from django.contrib.auth.mixins import LoginRequiredMixin



class ProductListView(ListView):

    model = Product
    context_object_name = 'products'
    template_name = 'product/product_list.html'