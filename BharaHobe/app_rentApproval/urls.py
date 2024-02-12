from django.urls import path, include
from . import views

urlpatterns = [
    path('admin_page/', views.admin_page, name='admin_page'),
    path('view_addproduct_rqsts/',views.add_product_rqsts,name='add_product_rqsts'),
    path('view_addproduct_rqsts/approve_product/<str:request_id>/',views.approve_product,name='approve_product'),
    path('view_addproduct_rqsts/disapprove_product/<str:request_id>/',views.disapprove_product,name='disapprove_product'),
   
]

