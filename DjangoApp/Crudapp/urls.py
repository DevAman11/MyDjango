from django.urls import path

from . import views

urlpatterns = [

    path('',views.Home),
    path('About/', views.About),
    path('Card',views.Card),
    path('Loan',views.Loan),
    path('Privacy',views.Privacy),
    path('Contact/',views.Contact),
    path('dynamic/<id>',views.dynamic)
]
