from django.urls import path
from . import views


urlpatterns = [
    path('',views.ProductListView.as_view(),name='product_list'),
    path('product-detail/<slug:slug>/<int:product_id>/',views.ProductDetailView.as_view(),
         name='product_detail'),
    path('product-update-view/<int:pk>/',views.ProductUpdateView.as_view(),name='product_update_view'),
    path('product-create-view/',views.ProductCreateView.as_view(),name='create_product_url')

]
