import json

from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
)

from rest_framework.views import APIView

from rest_framework.permissions import (
    AllowAny,
)

from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    PasswordResetSerializer,
    TokenSerializer,
    )
from rest_framework.authtoken.models import Token

from user.methods import Methods
from user.authentication import TokenMethods

User = get_user_model()
T = TokenMethods()
M = Methods()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            data = serializer.validated_data
            return Response(data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserLoginAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            return Response(data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class PasswordResetAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        response = M.password_reset(data)
        content = json.loads(response.content)
        return Response(content, status=response.status_code)


class TokenExpiredView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        try:
            token = request.data["token"]
            token = Token.objects.filter(key=token)[0]
        except:
            return Response("Invalid Token", HTTP_400_BAD_REQUEST)
        else:
            checker = T.is_token_expired(token)
            return Response({"expired": checker }, status=HTTP_200_OK)


class UserByTokenView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        try:
            token = request.data["token"]
            user_id = Token.objects.filter(key=token)[0].user_id
        except Exception as e:
            return Response("Invalid Token", HTTP_400_BAD_REQUEST)
        else:
            user_obj = User.objects.filter(id=user_id)[0]
            user_dict = M.to_dict(user_obj)
            user_res = {}
            user_res["username"] = user_dict["username"]
            user_res["email"] = user_dict["email"]
            user_res["phone"] = user_dict["phone"]
            return Response(user_res, status=HTTP_200_OK)













