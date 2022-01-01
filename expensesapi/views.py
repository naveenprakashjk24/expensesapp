from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ExpenseSerializer
from .models import Expense
from rest_framework import permissions
from .permissions import IsOwner


class ExpenseApiView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenseDeatilApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated,IsOwner,)
    lookup_field = 'id'

    def perform_create(self, serializer, id):
        return serializer.save(owner=self.request.user)

    def get_queryset(self, id ):
        return self.queryset.filter(owner=self.request.user)
