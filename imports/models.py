from django.db import models

class Imports (models.Model):
    taskCd = models.CharField(max_length=20)
    dclDe = models.CharField(max_length=10, blank=True, null=True)
    itemSeq = models.IntegerField()
    dclNo = models.CharField(max_length=50)
    hsCd = models.CharField(max_length=20)
    itemNm = models.CharField(max_length=100)
    imptItemsttsCd = models.CharField(max_length=10)
    orgnNatCd = models.CharField(max_length=5)
    exptNatCd = models.CharField(max_length=5)
    pkg = models.IntegerField()
    pkgUnitCd = models.CharField(max_length=10, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=2)
    qtyUnitCd = models.CharField(max_length=10)
    totWt = models.DecimalField(max_digits=12, decimal_places=2)
    netWt = models.DecimalField(max_digits=12, decimal_places=2)
    spplrNm = models.TextField()
    agntNm = models.CharField(max_length=100)
    invcFcurAmt = models.DecimalField(max_digits=15, decimal_places=2)
    invcFcurCd = models.CharField(max_length=10)
    invcFcurExcrt = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.itemNm
