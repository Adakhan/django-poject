from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from main.models import Product
from . import views

urlpatterns = [
    path('', ListView.as_view(queryset=Product.objects.all().order_by("-date"), template_name="account/posts.html")),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=Product, template_name="account/post.html")),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit, name='edit'),
    path('profile/password/', views.edit_password, name='edit_password'),
]
