from django.db import models
from django.utils import timezone
class TaskData(models.Model):
    fields = models.ForeignKey('MyFields',null=True,blank=True)
    data = models.ForeignKey('MyData',null=True,blank=True)



class MyFields(models.Model):
    did = models.CharField('id',unique=True, max_length=128,null=True,blank=True)
    label=models.CharField('id',unique=True, max_length=128,null=True,blank=True)
    type=models.CharField('id',unique=True, max_length=128,null=True,blank=True)


#Main Model In Question Above Models are Miscelleneous
class MyData(models.Model):
    device_name=models.CharField('device_name' ,max_length=128,null=True,blank=True)
    magnification=models.CharField('magnification', max_length=128,null=True,blank=True)
    field_of_view=models.CharField('field_of_view', max_length=128,null=True,blank=True)
    range=models.CharField('range', max_length=128,null=True,blank=True)
    created_date=models.DateField('created_date',default=timezone.now())