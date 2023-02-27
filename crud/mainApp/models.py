from django.db import models

class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=15)
    salary=models.IntegerField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    def ___str__(self):
        return str(self.id)+""+self.name+""+self.email