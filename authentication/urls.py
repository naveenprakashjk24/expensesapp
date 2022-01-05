from django.urls import path
from .views import RegisterApiview, VerifyEmail, LoginApiView, PasswordTokenCheckAPI, RequestPasswordRestEmail,SetNewPasswordAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterApiview.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('email_verify/', VerifyEmail.as_view(), name='email-verify'),
    path('taken/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('password-reset-request/', RequestPasswordRestEmail.as_view(), name='password-reset-request'),
    path('password-reset/<str:uidb64>/<str:token>/', PasswordTokenCheckAPI.as_view(), name='password-rest'),
    path('password-reset-complete/', SetNewPasswordAPIView .as_view(), name='password-reset-complete'),

]