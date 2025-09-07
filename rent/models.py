from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager



class CustomerManager(BaseUserManager):

    def create_user(self,login,password=None, **extra_feilds):
     if not login:
        raise ValueError ("Login email must be set")
     user=self.model(login=login,**extra_feilds)
     user.set_password(password)
     user.save(using=self._db)
     return user
    
    def create_superuser(self,login,password=None, **extra_fields):
       extra_fields.setdefault("is_superuser,True")
       extra_fields.setdefault("is_staff,True")
       return self.create_user(login, password, **extra_fields)

class Customer(AbstractUser,PermissionError):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    gmail = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    is_blocked = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    login = models.CharField(max_length=150, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["gmail", "phone"]

    objects = CustomerManager()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.login})"