from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.home,name='home'),
    path('products/', views.products, name='products'),
    path('search/', views.prod_search, name='prod_search'),
    path('products/', views.product_view, name='prod_page'),
    path('products/<int:id>', views.product_details, name='prod_details'),
    path('products/add', views.AddProduct.as_view(), name = 'add_prod'),
    path('products/edit/<int:pk>', views.EditProduct.as_view(), name = 'edit_prod'),
    path('products/del/<int:pk>', views.DelProduct.as_view(), name = 'del_prod'),
    path('products/search', views.searchView, name = 'prod_search')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




