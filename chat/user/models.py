from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, username , password = None):
        if not username:
            raise ValueError('User must have an username')
        if not password:
            raise ValueError('User must have an password')
        user = self.model(
            username = username 
        )
        user.set_password(password) 
        user.save(using = self._db)
        return user

    def create_superuser(self, username , password):
        user = self.create_user(
            username = username, 
            password = password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length = 100  , unique = True)
    password = models.CharField(max_length = 200)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['password']
    objects = UserManager()
    def __str__(self):
        return self.username
    def has_perm(self, perm, obj = None):
        return self.is_superuser
    def has_module_perms(self, app_label):
        return True




class Message(models.Model):
    sender       = models.ForeignKey(User, on_delete= models.CASCADE , related_name='sender')
    receiver     = models.ForeignKey(User, on_delete= models.CASCADE , related_name='receiver')
    content      = models.TextField()
    def __str__(self):
        return self.content