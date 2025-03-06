from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.home),
    path('products/', views.products, name='products'),
    path('search/', views.prod_search, name='prod_search')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


