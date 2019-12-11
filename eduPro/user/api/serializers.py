import json

from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
    )
from rest_framework import serializers, validators
from rest_framework.authtoken.models import Token

from user.methods import Methods
from user.authentication import TokenMethods

# for data_testing
# from lecture.factories import Factories
# F = Factories()
# F.factories()

User = get_user_model()
T = TokenMethods()
M = Methods()


class UserCreateSerializer(ModelSerializer):
    password = CharField(help_text='알파벳, 숫자, 특수문자 조합 8자 이상')
    phone = CharField(min_length=11, max_length=11, help_text='11자리의 유효한 핸드폰 번호')

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'username',
            'phone'
        ]
        extra_kwargs = {"password": {"write_only": True}}

    """
    validation error의 type이 다른 것과 다르게 한 층위가 더 더해져서 object식으로 온다고 해서 사용하지 않고, 
    제외 => 이런식으로도 key값별로 validate를 진행할수 있다. 
    """
    # def validate_phone(self, value):
    #     if len(value) != 11:
    #         raise ValidationError("전화번호를 올바르게 입력해 주세요.")
    #     for i in list(value):
    #         if type(int(i)) != int:
    #             raise ValidationError("전화번호를 올바르게 입력해 주세요.")
    #     return value

    def validate(self, data):
        username = data["username"]
        email = data["email"]
        phone = data["phone"]
        password = data["password"]
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"

        for i in list(phone):
            if type(int(i)) != int:
                raise ValidationError("전화번호를 올바르게 입력해 주세요.")

        if len(password) < 8 or not any(char in special_characters for char in password):
            raise ValidationError('Password must contain at least 8 letters(alphabet and number) and 1 special character')

        return data

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        phone = validated_data["phone"]
        password = validated_data["password"]

        user_obj = User(
            email=email,
            username=username,
            phone=phone
        )
        user_obj.set_password(password)
        user_obj.save()

        M.make_user_lecture_set(email)
        return


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = CharField(label="Email Address", required=False, allow_blank=True)
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'token'
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        password = data["password"]
        if not email:
            raise ValidationError("A email is required to login.")
        user_qs = User.objects.filter(email=email)
        if not user_qs:
            raise ValidationError("No user email to match")
        else:
            user_obj = user_qs[0]
        if not user_obj.check_password(password):
            raise ValidationError("Incorrect password please try again.")
        if Token.objects.filter(user=user_obj):
            """
            for test of token working well
            """
            # token = Token.objects.filter(user=user_obj).token
            # print('token', token)
            # left_time = T.expires_in(token)
            # print('left time', left_time)
            # checker = T.is_token_expired(token)
            # print('expired?', checker)
            Token.objects.filter(user=user_obj).delete()
        token = Token.objects.create(user=user_obj)
        is_expired, token = T.token_expire_handler(token)
        email = data["email"]
        payload = {"token": token.key,
                   "expiry": settings.EXPIRING_TOKEN_LIFESPAN}
        data["payload"] = payload
        M.update_lecture_apply(email)

        return data


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(help_text='토큰')
    class Meta:
        fields = ('token',)


class PasswordResetSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)




