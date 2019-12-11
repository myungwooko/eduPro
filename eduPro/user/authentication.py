from datetime import timedelta
from django.utils import timezone
from django.conf import settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


class TokenMethods:
    # this return left time
    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.EXPIRING_TOKEN_LIFESPAN) - time_elapsed
        return left_time

    # token checker if token expired or not
    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    # if token is expired new token will be established
    # If token is expired then it will be removed
    # and new one with different key will be created
    def token_expire_handler(self, token):
        is_expired = self.is_token_expired(token)
        if is_expired:
            token.delete()
            token = Token.objects.create(user=token.user)
        return is_expired, token


class ExpiringTokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")

        if not token.user.is_active:
            raise AuthenticationFailed("User is not active")

        T = TokenMethods()
        is_expired, token = T.token_expire_handler(token)
        if is_expired:
            raise AuthenticationFailed("The Token is expired")

        return (token.user, token)

