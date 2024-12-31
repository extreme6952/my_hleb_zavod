from django.urls import path
from . import views


urlpatterns = [
    path('',views.ProductListView.as_view(),name='product_list'),
    path('product-detail/<slug:slug>/<int:product_id>/',views.ProductDetailView.as_view(),
         name='product_detail')
]
