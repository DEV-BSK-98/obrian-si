from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    itemNm = models.CharField("Item Name", max_length=255)
    itemCd = models.CharField("Item Code", max_length=255)
    itemClsCd = models.CharField("Item Class Code", max_length=255)
    itemTyCd = models.CharField("Item Type Code", max_length=255)
    bcd = models.CharField("Item Type Code", max_length=255)
    orgnNatCd = models.CharField("Country Of Origin", max_length=255)
    pkgUnitCd = models.CharField("Packing Unit", max_length=100)
    qtyUnitCd = models.CharField("QTY Unit", max_length=100)
    vatCatCd = models.CharField("Tax Type Unit", max_length=100)
    iplCatCd = models.CharField("IPL Category Code", max_length=100)
    tlCatCd = models.CharField("TL Category Code", max_length=100)
    exciseTxCatCd = models.CharField("Excise Tax Category Code", max_length=100)

    def __str__(self):
        return f"{self.itemNm} ({self.itemCd})"
