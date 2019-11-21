from django.db import models
from bank.branch.models import Branch

class Customer (models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=200)

    branch = models.ForeignKey(
        Branch,
        on_delete = models.CASCADE
    )

    def __str__ (self):
        return(
            f"{self.customer_name} | {self.branch}"
        )