from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index,name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    # Product
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:pk>', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>', views.product_update, name='dashboard-product-update'),
    # order
    path('order/', views.order, name='dashboard-order'),
    path('purchase/order/', views.purchase_order, name='dashboard-purchase-order'),
    path('purchase/search/', views.search_purchase_order, name='dashboard-purchase-order-list'),
    path('client/order/', views.client_order, name='dashboard-client-order'),
    # client
    path('client/', views.client, name='dashboard-client'),
    path('client/update/<int:pk>', views.client_update, name='dashboard-client-update'),
    path('client/delete/<int:pk>', views.client_delete, name='dashboard-client-delete'),
    # supplier
    path('supplier/', views.supplier, name='dashboard-supplier'),
    path('supplier/update/<int:pk>', views.supplier_update, name='dashboard-supplier-update'),
    path('supplier/delete/<int:pk>', views.supplier_delete, name='dashboard-supplier-delete'),
    
]
# path('suppliers/', supplier_list, name='supplier_list'),
