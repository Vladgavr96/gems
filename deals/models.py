from django.db import models


class Deal(models.Model):
    customer = models.CharField(max_length=256)
    item = models.CharField(max_length=256)
    total = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    deal_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.customer} {self.deal_date}'

class UploadedData(models.Model):
    file = models.FileField
