from django.urls import path
from jinjaaap import views

urlpatterns = [
    path('',views.home,name='My_home'),
    path('about/',views.about,name='My_about'),
    path('contact/',views.contact,name='My_contact'),
    path('gallery/',views.gallery,name='My_gallery')
]