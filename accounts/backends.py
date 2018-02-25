from django.contrib.auth.backends import ModelBackend

from accounts.models import User


class UserAuthenticationBackend(ModelBackend):
    """
    Authenticate against Contact models.
    """

    def authenticate(self, email=None, name=None):
        """
        Checks if given credentials are valid and return the user
        """
        user = None
        try:
            user = User.objects.get(email__iexact=email, is_active=True)
        except User.DoesNotExist:
            user = User.objects.create_user(email, name)

        return user


    def get_user(self, user_id):
        """
        Gets an user by given id
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
