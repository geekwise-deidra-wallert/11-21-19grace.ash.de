from django.db import models

class Branch (models.Model):

    class Meta:
        verbose_name_plural: 'Branches'

    branch_name = models.CharField(max_length=100)
    location_city = models.CharField(max_length=50)
    location_id = models.CharField(max_length=25)

    def __str__(self):
        return (
            f"Branch Name: {self.branch_name} | City: {self.location_city}"
        )
