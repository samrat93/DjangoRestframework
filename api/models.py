from django.db import models

# Create your models here.

companyTypes = (
    ("IT","Software"),
    ("corporation","Corporation"),
    ("cooperative","Cooperative"),
    )

employeePositon = (
    ("fe","FrontEnd Software Developer"),
    ("be","Backend Software Developer"),
    ("manager","Project Manager"),
    ("ceo","Chief Executive Officer"),
    ("cto","Chief Technical Officer"),
)

class Company(models.Model):
    """ Model for company table """

    companyId = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(companyTypes))
    addedDate = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.companyName

class Employee(models.Model):
    """ Model for employee table """

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    about = models.TextField()
    position = models.CharField(max_length =50, choices=(employeePositon))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
