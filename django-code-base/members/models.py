from django.db import models

# Create your models here.
# IMPORTS
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
import uuid
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

mobileRegex= "^(\+\d{1,3}[- ]?)?\d{10}$"

class MyMemberManager(BaseUserManager):
    def create_user(self, email, name, rollNo, password = None):
        if not email:
            raise ValueError("Email address required")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            rollNo=rollNo,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, rollNo, password=None):
        user = self.create_user(email, name, rollNo, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Member(AbstractBaseUser):

    id = models.UUIDField(default=uuid.uuid4, editable=False)
    date_joined = models.DateTimeField(default=timezone.now)
    name = models.CharField("Name", max_length=40)
    email = models.EmailField(primary_key=True, max_length=255, unique=True, verbose_name="Email Address")
    mobile = models.CharField(
        max_length=16,
        validators=[
            RegexValidator(
                regex=mobileRegex,
                message="Enter a valid mobile number",
                code="invalid_mobile"
            )
        ],
    )
    rollNo = models.CharField(max_length=10)
    degree = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyMemberManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "rollNo"]
    
    def __str__(self):
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True