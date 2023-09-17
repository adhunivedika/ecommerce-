from django.urls import path

import shop
from .import views
app_name='shop'
urlpatterns = [

    path('',views.allProdcat,name='allProdcat'),
    path('<slug:c_slug>/',views.allProdcat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodcatdetail,name='prodcatdetail')

]