from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings

app_name="account"

urlpatterns = [
    # previous login
    # path('login/', views.user_login, name='login'),

    # login / logout
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     # password change
#     path('password-change/', auth_views.PasswordChangeView.as_view(),
#          name='password_change'),
#     path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(),
#          name='password_change_done'),
#     # password reset (email)
#     path('password-reset/', auth_views.PasswordResetView.as_view(),
#          name='password_reset'),
#     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
#          name='password_reset_done'),
#     path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
#          name='password_reset_confirm'),
#     path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(),
#          name='password_reset_complete'),
    # User home
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    #path('', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    # Profile
    path('profile/<pk>/update', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/<pk>', views.ProfileDetailView.as_view(), name='profile_detail'),
    # Settings
    path('settings/<pk>', views.SettingsDetailView.as_view(), name='settings_detail'),
]