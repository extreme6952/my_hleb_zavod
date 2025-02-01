from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.base import TemplateResponseMixin,View
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from .models import *
from .forms import *


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/product_list.html'
    
class ProductDetailView(LoginRequiredMixin,View):
    def get(self,request,slug,product_id):
        product = get_object_or_404(Product,
                                    slug=slug,
                                    id=product_id)
        return render(request,
                      'product/product_detail.html',
                      {'product':product})

class ProductUpdateView(TemplateResponseMixin, LoginRequiredMixin, View):
    product = None
    template_name = 'product/forms_files_template/update_product_database.html'

    def get_form(self, data=None, files=None):
        return UpdateProductInformationForm(instance=self.product, data=data, files=files)

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.product = get_object_or_404(Product, id=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return self.render_to_response({
            'product': self.product,
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = self.get_form(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)

        return self.render_to_response({
            'product': self.product,
            'form': form,
        })


class ProductCreateView(LoginRequiredMixin,TemplateResponseMixin,View):

    template_name = 'product/forms_files_template/create_product_form.html'
    
    def get_form(self,data=None,files=None):

        return ProductCreateForm(data=data,
                                 files=files)
    
    def get(self,*args, **kwargs):

        form = self.get_form()
        return self.render_to_response(
            {'form':form}
        )
    
    def post(self,request,*args, **kwargs):
        
        form = self.get_form(data=request.POST,
                             files=request.FILES)
        
        if form.is_valid():
            form.save()

        return self.render_to_response(
            {'form':form}
        )