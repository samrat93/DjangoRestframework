from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.

companyTypes = (
    ("IT", "Software"),
    ("corporation", "Corporation"),
    ("cooperative", "Cooperative"),
)

employeePositon = (
    ("fe", "FrontEnd Software Developer"),
    ("be", "Backend Software Developer"),
    ("manager", "Project Manager"),
    ("ceo", "Chief Executive Officer"),
    ("cto", "Chief Technical Officer"),
)

STATE_CHOICE = ((
    ("Gujarat", "Gujarat"),
    ("Delhi", "Delhi"),
    ("Uttar Pardesh", "Uttar Pardesh"),
    ("Bihar", "Bihar"),
    ("West Bangal", "West Bangal"),
    ("Jharkhand", "Jharkhand")
))


#  Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# custom user model


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    state = models.CharField(choices=STATE_CHOICE, max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)
    pimage = models.ImageField(upload_to='pimages', blank=True)
    docs = models.FileField(upload_to='docs', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Company(models.Model):
    """ Model for company table """

    companyId = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(companyTypes))
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
    position = models.CharField(max_length=50, choices=(employeePositon))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
