from django.db import models

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

    def __str__(self):
        return f"SAR {self.sarNo} - {self.regTyCd}"

class SAR_Item(models.Model):
    sar = models.ForeignKey(SAR, related_name='sar_itemList', on_delete=models.CASCADE)
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
