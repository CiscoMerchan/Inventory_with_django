from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index,name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('product/', views.product, name='dashboard-product'),
    path('order/', views.order, name='dashboard-order'),
    path('client/', views.client, name='dashboard-client'),
    path('supplier/', views.supplier, name='dashboard-supplier'),
    
]
# path('suppliers/', supplier_list, name='supplier_list'),
