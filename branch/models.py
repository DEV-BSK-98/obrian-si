from django.db import models
from datetime import date

# Create your models here.
class Branch (models.Model):
    branch_name = models.CharField(max_length=100, null=True, verbose_name="T-Pin")
    bhfId = models.CharField(max_length=255, null=True, verbose_name="Your Name")
    
    def __str__(self):
        return f"{self.branch_name} - {self.bhfid}"