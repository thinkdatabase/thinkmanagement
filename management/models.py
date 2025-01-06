from django.db import models
from django.contrib.auth.models import AbstractUser



class InstitutionModel(models.Model):
    name=models.CharField(max_length=200)
    place=models.CharField(max_length=200)

class DepartmentModel(models.Model):
    name=models.CharField(max_length=100)


class DivisionModel(models.Model):
    name=models.CharField(max_length=100)

class MaterialModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    file=models.FileField(upload_to='files',null=True)

class ProductModel(models.Model):
    name=models.CharField(max_length=100)
    material=models.ManyToManyField(MaterialModel)
    

class BatchModel(models.Model):
    name=models.CharField(max_length=200)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)

class User(AbstractUser):
    phone=models.PositiveIntegerField(null=True)
    institute=models.OneToOneField(InstitutionModel,on_delete=models.CASCADE,null=True)
    department=models.OneToOneField(DepartmentModel,on_delete=models.CASCADE,null=True)
    divison=models.OneToOneField(DivisionModel,on_delete=models.CASCADE,null=True)


class StudentModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    batch=models.ForeignKey(BatchModel,on_delete=models.CASCADE,null=True)




    

