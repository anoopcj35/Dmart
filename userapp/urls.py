from.import views
from django.urls import path

urlpatterns=[

    path('',views.user,name='user'),
    path('uproducts',views.uproducts,name='uproducts'),
    path('ucategories',views.ucategories,name='ucategories'),
    path('ucontact',views.ucontact,name='ucontact'),
    path('ureg',views.ureg,name='ureg'),
    path('ulogin',views.ulogin,name='ulogin'),   
    path('regdata',views.regdata,name='regdata'),
    path('memberlogin',views.memberlogin,name='memberlogin'),
    path('memberlogout',views.memberlogout,name='memberlogout'),
    path('uprodetails/<int:id>/',views.uprodetails,name='uprodetails'),
    path('userdata/<int:id>',views.userdata,name='userdata'),
    path('ucart/',views.ucart,name='ucart'),
    path('ucdelete/<int:id>',views.ucdelete,name='ucdelete'), 
    path('ucheckout/',views.ucheckout,name='ucheckout'),
    path('ucdata/',views.ucdata,name='ucdata'),
    path('uabout/',views.uabout,name='uabout'),
    path('contactdata/',views.contactdata,name='contactdata'),
    


]