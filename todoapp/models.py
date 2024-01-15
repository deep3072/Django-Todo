from django.db import models

# Create your models here.

class todo(models.Model):
    name = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True) # added or edited
    def __str__(self):
        return self.name
