from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, organization_id, is_active, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)

        user = self.model(
            id=str(uuid4()),
            email=email,
            first_name=first_name,
            last_name=last_name,
            organization_id=organization_id,
            is_active=is_active
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, organization, password):
        user = self.create_user(email, first_name, last_name, organization, True, password)

        return user


class Organization(models.Model):
    name = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "organization"


class ApplicationUser(AbstractBaseUser):

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    REQUIRED_FIELDS = ["first_name", "last_name", "organization"]
    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    identifier = models.CharField(max_length=36, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64, blank=False, null=False)
    last_name = models.CharField(max_length=64, blank=False, null=False)
    organization = models.ForeignKey(Organization, null=False, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, app_label):
        return True

    class Meta:
        db_table = "application_user"
