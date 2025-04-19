from django.db import models

class SAR_Item(models.Model):
    itemSeq = models.IntegerField()
    itemCd = models.CharField(max_length=50)
    itemClsCd = models.CharField(max_length=50)
    itemNm = models.CharField(max_length=255)
    pkgUnitCd = models.CharField(max_length=50)
    qtyUnitCd = models.CharField(max_length=50)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    prc = models.DecimalField(max_digits=10, decimal_places=2)
    splyAmt = models.DecimalField(max_digits=10, decimal_places=2)
    taxblAmt = models.DecimalField(max_digits=10, decimal_places=2)
    vatCatCd = models.CharField(max_length=50)
    taxAmt = models.DecimalField(max_digits=10, decimal_places=2)
    totAmt = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item {self.itemNm} ({self.itemCd})"

class SAR(models.Model):
    tpin = models.CharField(max_length=15)
    bhfId = models.CharField(max_length=10)
    sarNo = models.IntegerField()
    orgSarNo = models.IntegerField()
    regTyCd = models.CharField(max_length=10)
    custTpin = models.CharField(max_length=15, null=True, blank=True)
    custNm = models.CharField(max_length=255, null=True, blank=True)
    custBhfId = models.CharField(max_length=10, null=True, blank=True)
    sarTyCd = models.CharField(max_length=10)
    ocrnDt = models.CharField(max_length=8)
    totItemCnt = models.IntegerField()
    totTaxblAmt = models.DecimalField(max_digits=10, decimal_places=4)
    totTaxAmt = models.DecimalField(max_digits=10, decimal_places=4)
    totAmt = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.TextField(null=True, blank=True)
    regrId = models.CharField(max_length=50)
    regrNm = models.CharField(max_length=255)
    modrNm = models.CharField(max_length=255)
    modrId = models.CharField(max_length=50)

    listItem=models.ManyToManyField (SAR_Item, blank=True)

    def __str__(self):
        return f"SAR {self.sarNo} - {self.regTyCd}"

# class EntryItemList (models.Model):
#     itemSeq = models.CharField (max_length=255, default="", null=True)
#     itemCd = models.CharField (max_length=255, default="", null=True)
#     itemClsCd = models.CharField (max_length=255, default="", null=True)
#     itemNm = models.CharField (max_length=255, default="", null=True)
#     pkgUnitCd = models.CharField (max_length=255, default="", null=True)
#     qtyUnitCd = models.CharField (max_length=255, default="", null=True)
#     qty = models.FloatField (default=0.00, null=True)
#     prc = models.DecimalField (default=0.00, max_digits=11, decimal_places=2, null=True)
#     splyAmt = models.DecimalField (default=0.00, max_digits=11, decimal_places=2, null=True)
#     taxblAmt = models.DecimalField (default=0.00, max_digits=11, decimal_places=2, null=True)
#     vatCatCd = models.CharField (max_length=255, default="", null=True)
#     taxAmt = models.DecimalField (default=0.00, max_digits=11, decimal_places=2, null=True)
#     totAmt = models.DecimalField (default=0.00, max_digits=11, decimal_places=2, null=True)

# class StockEntry (models.Model):
#     tpin = models.CharField(max_length=50, default="", null=True)
#     bhfId =models.CharField(max_length=50, default="", null=True)
#     sarNo =models.CharField(max_length=50, default="", null=True)
#     orgSarNo =models.CharField(max_length=50, default="", null=True)
#     regTyCd =models.CharField(max_length=50, default="", null=True)
#     custTpin =models.CharField(max_length=50, default="", null=True)
#     custNm =models.CharField(max_length=50, default="", null=True)
#     custBhfId =models.CharField(max_length=50, default="", null=True)
#     sarTyCd =models.CharField(max_length=50, default="", null=True)
#     ocrnDt =models.CharField(max_length=50, default="", null=True)
#     totItemCnt =models.IntegerField(default=0, null=True)
#     totTaxblAmt =models.DecimalField(default=0.00, max_digits=11, null=True, decimal_places=2)
#     totTaxAmt =models.DecimalField(default=0.00, max_digits=11, null=True, decimal_places=2)
#     totAmt =models.DecimalField(default=0.00, max_digits=11, null=True, decimal_places=2)
#     remark = models.TextField (blank=True)
#     regrNm =models.CharField(max_length=50, default="", null=True)
#     regrId =models.CharField(max_length=50, default="", null=True)
#     modrNm =models.CharField(max_length=50, default="", null=True)
#     modrId =models.CharField(max_length=50, default="", null=True)

#     itemList = models.ManyToManyField (EntryItemList, blank=True)


class StockEntry (models.Model):
    item_name = models.CharField(max_length=50, default="", null=True)
    item_code =models.CharField(max_length=50, default="", null=True)
    in_qty =models.FloatField(default=0.00, null=True)
    out_qty =models.FloatField(default=0.00, null=True)
    current_qty =models.FloatField(default=0.00, null=True)
    in_value =models.FloatField(default=0.00, null=True)
    out_value =models.FloatField(default=0.00, null=True)
    current_value =models.FloatField(default=0.00, null=True)
    unit_price =models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True)