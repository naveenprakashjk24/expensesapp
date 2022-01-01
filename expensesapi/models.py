from django.db import models
from authentication.models import User


# Create your models here.


class Expense(models.Model):
    CATEGORY_OPTIONS = [('ONLINE_SERVICES', 'ONLINE_SERVICES'), ('TRAVEL', 'TRAVEL'),
                        ('FOOD', 'FOOD'), ('OTHERS', 'OTHERS')]

    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=200)
    amount = models.DecimalField(decimal_places=3, max_digits=10)
    description = models.TextField(max_length=350)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False,blank=False)
