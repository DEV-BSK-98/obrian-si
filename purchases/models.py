from django.db import models

class Purchase(models.Model):
    spplrTpin = models.CharField(max_length=15)
    spplrNm = models.CharField(max_length=255)
    spplrBhfId = models.CharField(max_length=10)
    spplrInvcNo = models.IntegerField()
    rcptTyCd = models.CharField(max_length=10)
    pmtTyCd = models.CharField(max_length=10)
    cfmDt = models.DateTimeField()
    salesDt = models.CharField(max_length=8)
    stockRlsDt = models.DateTimeField(null=True, blank=True)
    totItemCnt = models.IntegerField()
    totTaxblAmt = models.DecimalField(max_digits=10, decimal_places=4)
    totTaxAmt = models.DecimalField(max_digits=10, decimal_places=4)
    totAmt = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Invoice {self.spplrInvcNo} - {self.spplrNm}"

class LineItems(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='purchase_itemList', on_delete=models.CASCADE)
    itemSeq = models.IntegerField()
    itemCd = models.CharField(max_length=50)
    itemClsCd = models.CharField(max_length=50)
    itemNm = models.CharField(max_length=255)
    bcd = models.CharField(max_length=50, null=True, blank=True)
    pkgUnitCd = models.CharField(max_length=50)
    pkg = models.DecimalField(max_digits=5, decimal_places=2)
    qtyUnitCd = models.CharField(max_length=50)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    prc = models.DecimalField(max_digits=10, decimal_places=2)
    splyAmt = models.DecimalField(max_digits=10, decimal_places=2)
    dcRt = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    dcAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vatCatCd = models.CharField(max_length=50)
    iplCatCd = models.CharField(max_length=50, null=True, blank=True)
    tlCatCd = models.CharField(max_length=50, null=True, blank=True)
    exciseTxCatCd = models.CharField(max_length=50, null=True, blank=True)
    vatTaxblAmt = models.DecimalField(max_digits=10, decimal_places=2)
    exciseTaxblAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    iplTaxblAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tlTaxblAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    taxblAmt = models.DecimalField(max_digits=10, decimal_places=2)
    vatAmt = models.DecimalField(max_digits=10, decimal_places=2)
    iplAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tlAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    exciseTxAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totAmt = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item {self.itemNm} ({self.itemCd})"

class Import_Purchase(models.Model):
    spplrTpin = models.CharField(max_length=15)
    spplrNm = models.CharField(max_length=255)
    spplrBhfId = models.CharField(max_length=10)
    spplrInvcNo = models.IntegerField()
    rcptTyCd = models.CharField(max_length=10)
    pmtTyCd = models.CharField(max_length=10)
    cfmDt = models.DateTimeField()
    salesDt = models.CharField(max_length=8)
    stockRlsDt = models.DateTimeField(null=True, blank=True)
    totItemCnt = models.IntegerField()
    totTaxblAmt = models.DecimalField(max_digits=10, decimal_places=4)
    totTaxAmt = models.DecimalField(max_digits=10, decimal_places=4)
    totAmt = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Invoice {self.spplrInvcNo} - {self.spplrNm}"

class Import_LineItems(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='import_purchase_itemList', on_delete=models.CASCADE)
    itemSeq = models.IntegerField()
    itemCd = models.CharField(max_length=50)
    itemClsCd = models.CharField(max_length=50)
    itemNm = models.CharField(max_length=255)
    bcd = models.CharField(max_length=50, null=True, blank=True)
    pkgUnitCd = models.CharField(max_length=50)
    pkg = models.DecimalField(max_digits=5, decimal_places=2)
    qtyUnitCd = models.CharField(max_length=50)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    prc = models.DecimalField(max_digits=10, decimal_places=2)
    splyAmt = models.DecimalField(max_digits=10, decimal_places=2)
    dcRt = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    dcAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vatCatCd = models.CharField(max_length=50)
    iplCatCd = models.CharField(max_length=50, null=True, blank=True)
    tlCatCd = models.CharField(max_length=50, null=True, blank=True)
    exciseTxCatCd = models.CharField(max_length=50, null=True, blank=True)
    vatTaxblAmt = models.DecimalField(max_digits=10, decimal_places=2)
    exciseTaxblAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    iplTaxblAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tlTaxblAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    taxblAmt = models.DecimalField(max_digits=10, decimal_places=2)
    vatAmt = models.DecimalField(max_digits=10, decimal_places=2)
    iplAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tlAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    exciseTxAmt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totAmt = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item {self.itemNm} ({self.itemCd})"
