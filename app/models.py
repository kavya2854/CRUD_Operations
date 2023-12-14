from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno = models.IntegerField(primary_key = True)
    dname = models.CharField(max_length = 100)
    loc = models.CharField(max_length = 100)
    deptblock = models.CharField(max_length = 100,default = 'A')
    
    def __str__(self):
        return self.dname+self.loc

class Employee(models.Model):
    empno = models.IntegerField(primary_key = True)
    ename = models.CharField(max_length = 100)
    job = models.CharField(max_length = 100)
    mgr =  models.IntegerField()
    hiredate = models.DateField()
    sal = models.IntegerField()
    comm = models.IntegerField(null = True,blank = True)
    deptno = models.ForeignKey(Dept,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.ename+self.job