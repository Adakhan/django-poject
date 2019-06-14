from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from main.models import Product
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from . import views

urlpatterns = [
    path('', ListView.as_view(queryset=Product.objects.all().order_by("-date"), template_name="main/posts.html")),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=Product, template_name="main/post.html")),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', LoginView.as_view(template_name='main/enter.html'), name="login"),
    path('registration/', views.UserFormView.as_view(), name='registration'),
    path('reset-password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done/', PasswordResetDoneView.as_view(), name='reset_password_done'),
    re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,23})/$',
            PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
