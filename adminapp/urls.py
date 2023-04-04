from django.urls import path
from.import views

urlpatterns = [
    path('',views.admin,name='admin'),
    path('productform/',views.productform,name='productform'),
    path('categoryform/',views.categoryform,name='categoryform'),
    path('productdata/',views.productdata,name='productdata'),
    path('categorydata/',views.categorydata,name='categorydata'),
    path('producttable/',views.producttable,name='producttable'),
    path('categorytable/',views.categorytable,name='categorytable'),
    path('productedit/<int:id>/',views.productedit,name='productedit'),
    path('categoryedit/<int:id>/',views.categoryedit,name='categoryedit'),
    path('productupdate/<int:id>/',views.productupdate,name='productupdate'),
    path('categoryupdate/<int:id>/',views.categoryupdate,name='categoryupdate'),
    path('productdelete/<int:id>/',views.productdelete,name='productdelete'),
    path('categorydelete/<int:id>/',views.categorydelete,name='categorydelete'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adlogin/',views.adlogin,name='adlogin'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('adlogout/',views.adlogout,name='adlogout'),
    path('user_data',views.user_data,name='user_data'),
    path('order_data',views.order_data,name='order_data'),
    path('contact_data',views.contact_data,name='contact_data'),

]