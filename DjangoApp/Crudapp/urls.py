from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('Home',views.Home),
    path('Blog',views.Blog),
    path('Contact/',views.Contact),
    path('About/', views.About),
    path('dynamic/<id>',views.dynamic)
]
