from django.urls import path
from . import views
from .views import map_view, map_log_view, profile
from .views import (
    register,
    login_view,
    CustomPasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.contrib.auth.views import LogoutView
#tests
urlpatterns = [
    path('', map_view, name='map'),  # This should render index.html
    #path('mainpage/', views.desktop_one, name='desktop_one'),  # This should render DesktopOne.html
    #path('mainpagelog/', views.desktop_onelog, name='desktop_onelog'),  # This should render DesktopOne.html

    path('map/', map_view, name='map'),
    path('logout/', LogoutView.as_view(next_page='map'), name='logout'),
    path('maplog/', map_log_view, name='maplog'),
    #path('sign-in/', views.desktop_two, name='desktop_two'),
    #path('forgot-password/', views.desktop_three, name='desktop_three'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('mapprofile/', views.map_profile_view, name='mapprofile'),

    # Custom password reset flow
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='myappp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='myappp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='myappp/password_reset_complete.html'), name='password_reset_complete'),

    path('favorites/', views.favorites_view, name='favorites_view'),
]
