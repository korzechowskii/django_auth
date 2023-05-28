from django.contrib import admin
from django.urls import path
from auth_system import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup', views.signup_page, name='signup_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),

    path('publicpage', views.public_page, name='public_page'),
    path('privatepage', views.private_page, name='private_page'),
    path('privateclasspage', views.PrivateClass_page.as_view(), name='privateclass_page'),
]