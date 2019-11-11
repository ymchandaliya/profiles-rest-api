from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.

class UserProfileManager(BaseUserManager):
    '''user profile manager'''

    def create_user(self,email,name,password=None):
        '''creating user model'''
        if not email:
            raise ValueError("Email field is required")

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        '''creating superuser for user profile'''

        user=self.create_user(email,name,password)

        user.is_staff=True
        user.is_superuser=True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    '''Database model for users in thr system'''

    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Retrieve full name of user'''
        return self.name

    def get_short_name(self):
        '''Retrieve short name of the user'''
        return self.name

    def __str__(self):
        return self.email

class ProfileFeedItem(models.Model):
    '''Profile status update'''
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''return model as string'''
        return self.status_text
