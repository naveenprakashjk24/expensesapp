from django.urls import path
from .views import ExpenseApiView, ExpenseDeatilApiView

urlpatterns = [
    path('', ExpenseApiView.as_view(), name='expense'),
    path('<int:id>/', ExpenseDeatilApiView.as_view(), name='expense-details'),
]