import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Extending the existing UserClass to create a custom User
class UserManager(BaseUserManager):

    def create_user(self, email, firstName, lastName, company, dob, password=None, ):
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
            firstName=firstName,
            lastName=lastName,
            company=company,
            dob=dob
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Manager(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=False
    )
    firstName = models.CharField(max_length=255, blank=False, default="null")
    lastName = models.CharField(max_length=255, blank=False, default="null")
    address = models.CharField(max_length=255, blank=False, default="null")
    dob = models.DateField(blank=False)
    company = models.CharField(max_length=255, blank=False, default="null")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "Manager"


# Employee Models
class Employee(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    firstName = models.CharField(max_length=255, blank=False, default="null")
    lastName = models.CharField(max_length=255, blank=False, default="null")
    email = models.EmailField(blank=False, unique=True, max_length=255)
    password = models.CharField(max_length=255, blank=False, default="null")
    mobile = models.CharField(max_length=10, blank=False, default="null")
    address = models.CharField(max_length=255, blank=False, default="null")
    dob = models.DateField(blank=False)
    company = models.CharField(max_length=128, blank=False, default="null")
    city = models.CharField(max_length=30, blank=False, default="null")
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Employee'
