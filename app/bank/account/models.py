from django.db import models

class Account (models.Model):
    account_choices = (
        ('checking', 'CHECKING'),
        ('savings', 'SAVINGS'),
        ('none', 'NONE'),
    )
    account_choices_params = models.CharField(
        max_length = 8,
        choices = account_choices,
        default= account_choices[0]
    )

    def __str__(self):
        return (
            f"{self.account_choices}"
        )