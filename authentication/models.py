from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.


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

    identifier = models.CharField(max_length=36, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64, blank=False, null=False)
    last_name = models.CharField(max_length=64, blank=False, null=False)
    organization = models.ForeignKey(Organization, null=False, on_delete=models.PROTECT)
    is_deleted = models.BooleanField(default=False, null=False)


    class Meta:
        db_table = "application_user"