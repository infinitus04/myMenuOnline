from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.clientLogin, name='clientLogin'),
    path('logout/', views.clientLogout, name='clientLogout'),
    path('psudoPanel/', views.psudoPanel, name='psudoPanel'),

    path('category/', views.categoryList, name='categoryList'),
    path('category/add/', views.categoryAdd, name='categoryAdd'),
    path('category/<int:id>/', views.categoryEdit, name='category'),
    # path('category/', views.categoryList, name='categoryList'),

    path('items/category=<int:id>/', views.itemList, name= 'itemList'),
    path('items/category=<int:id>/add/', views.itemAdd, name= 'itemAdd'),
    path('items/category=<int:id>/edit/item=<int:itemId>/', views.itemEdit, name= 'itemEdit'),

]
