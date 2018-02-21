from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email=None, name=None, is_active=True):
        """
        Creates and saves an User
        """

        user = self.model(
            email=email,
            name=name,
            is_active=is_active,
        )

        user.save(using=self._db)

        return user



class User(AbstractBaseUser):
    uid = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=50)
    uni = models.CharField(max_length=50)

    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)

    USERNAME_FIELD = 'email'

    # method to to edit users
    objects = UserManager()
