from django.urls import path
from .views import ExpenseApiView, ExpenseDetailApiView

urlpatterns = [
    path('', ExpenseApiView.as_view(), name='expense'),
    path('<int:id>/', ExpenseDetailApiView.as_view(), name='expense-details'),
]