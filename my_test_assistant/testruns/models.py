from django.db import models

from testcases.models import TestCase

# Create your models here.
class TestRun(models.Model):
    distroName=models.CharField(max_length=128)
    setup=models.CharField(max_length=512)

    def __unicode__(self):
        return "{0} {1}".format(self.distroName, self.setup)

class Task(models.Model):
    test=models.OneToOneField(TestCase, on_delete=models.CASCADE,)
    testRun=models.OneToOneField(TestRun, on_delete=models.CASCADE,)

    def __unicode__(self):
        return "{0} {1}".format(self.test, self.testRun)
