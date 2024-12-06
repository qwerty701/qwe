from django.contrib.messages import success
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_view
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('users-cart/', views.UserCartView.as_view(), name='users_cart'),
    path('logout/', views.logout, name='logout'),

    # url-адреса смены пароля
     path('password-change/',
     auth_view.PasswordChangeView.as_view(
     success_url='done/'
     ),
     name='password_change'),
     path('password-change/done/',
     auth_view.PasswordChangeDoneView.as_view(),
     name='password_change_done'),
]