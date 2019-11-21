from django.contrib import admin
from bank.account.models import Account
from bank.branch.models import Branch

admin.site.register(Account)
admin.site.register(Branch)