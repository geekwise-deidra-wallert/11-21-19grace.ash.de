from django.contrib import admin
from bank.account.models import Account
from bank.branch.models import Branch
from bank.customer.models import Customer

admin.site.register(Account)
admin.site.register(Branch)
admin.site.register(Customer)