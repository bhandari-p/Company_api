from django.db import models

# Create your models here.
# creating company model
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('NON IT','NON IT'),('MOBILE PHONES','MOBILE PHONES')))
    added_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

# creating employee model
class Employee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=24)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    company=models.ForeignKey( Company , on_delete=models.CASCADE)

    