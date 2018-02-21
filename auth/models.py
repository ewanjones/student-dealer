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
    uid = models.primaryKey()
    name = models.charField()
    email = models.charField()
    uni = models.charField()

    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    USERNAME_FIELD = 'email'

    # method to to edit users
    objects = UserManager()
