from django.urls import path
from .views import RegisterApiview, VerifyEmail, LoginApiView

urlpatterns = [
    path('register/', RegisterApiview.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('email_verify/', VerifyEmail.as_view(), name='email-verify'),

]