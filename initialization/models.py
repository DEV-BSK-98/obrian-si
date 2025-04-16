from django.db import models
from datetime import date

# Create your models here.
class Configurations (models.Model):
    tpin = models.CharField(max_length=100, null=True, verbose_name="T-Pin")
    taxprNm = models.CharField(max_length=255, null=True, verbose_name="Your Name")
    bsnsActv = models.CharField(max_length=255, null=True, verbose_name="Your Business Activity")
    bhfId = models.CharField(max_length=50, null=True, verbose_name="Branch ID")
    bhfNm = models.CharField(max_length=255, null=True, verbose_name="Branch Name")
    bhfOpenDt = models.DateField(default=date.today, null=True, verbose_name="Initialized On")
    prvncNm = models.CharField(max_length=100, null=True, verbose_name="Business Province")
    dstrtNm = models.CharField(max_length=100, null=True, verbose_name="Business District")
    sctrNm = models.CharField(max_length=100, null=True, verbose_name="Business Sector")
    dvcid = models.CharField(max_length=100, null=True, verbose_name="Device ID")
    vsdc_url = models.CharField(max_length=100, null=True, verbose_name="VSDC URL")

    def __str__(self):
        return f"{self.taxprNm} - {self.tpin}"