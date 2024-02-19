from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('reset/', views.password_reset, name='password_reset'),
    path('reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/complete/', views.password_reset_complete, name='password_reset_complete'),
]