from django.urls import path
from django.contrib.auth import views
from . import views as account_views

urlpatterns = [
    # path('login/', views.user_login, name='login')
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', account_views.dashboard, name='dashboard'),
    path('password_change/',
         views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
]
