from django.db import models

# Create your models here.
class Hyd_jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
class Pune_jobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
class Bang_jobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
