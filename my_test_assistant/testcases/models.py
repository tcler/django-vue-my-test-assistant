from django.db import models

# Create your models here.
class TestCase(models.Model):
    path=models.CharField(max_length=512)
    params=models.CharField(max_length=512)
    hostRequires=models.CharField(max_length=512)

    #attr
    component=models.CharField(max_length=128)
    testType=models.CharField(max_length=64)
    tier=models.IntegerField
    maxTime=models.TimeField
    engrossJob=models.BooleanField
    archIn=models.CharField(max_length=128)
    archNotIn=models.CharField(max_length=128)
    distroIn=models.CharField(max_length=128)
    distroNotIn=models.CharField(max_length=128)
    disable=models.BooleanField

    def __unicode__(self):
        return "{0} {1} {2}".format(self.path, self.params, self.hostRequires)

