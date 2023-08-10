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

    path('items/<int:id>/', views.itemList, name= 'itemList'),
    path('items/<int:id>/add/', views.itemAdd, name= 'itemAdd'),
    path('items/<int:id>/edit/<int:itemId>/', views.itemEdit, name= 'itemEdit'),

]
