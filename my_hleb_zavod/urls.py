from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('inventory.urls')),
    path('account/',include('account.urls',namespace="account"))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
