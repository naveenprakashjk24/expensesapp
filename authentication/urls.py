from django.urls import path
from .views import RegisterApiview, VerifyEmail

urlpatterns = [
    path('register/', RegisterApiview.as_view(), name='register'),
    path('email_verify/', VerifyEmail.as_view(), name='email-verify'),

]