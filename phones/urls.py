from django.urls import path

from phones import views

urlpatterns =[
    path('', views.index, name='home'),
    path('fileexport', views.export, name='fileexport'),
    path('webscrapping', views.webscrap, name='webscrapping'),
]