from django.db import models

class List_Items(models.Model):
    item_name = models.CharField(max_length=50, unique=True)
    item_cost = models.DecimalField(decimal_places=2, max_digits=15)
    item_purchased = models.BooleanField(default=False)
    item_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name

    def get_active_items():
        return List_Items.objects.filter(item_deleted=False).values()
