from django.urls import path, include

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    PasswordResetAPIView,
    TokenExpiredView,
    UserByTokenView,
)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name="login"),
    path('password_reset/', PasswordResetAPIView.as_view(), name="reset"),
    path('token_expired/', TokenExpiredView.as_view()),
    path('user_by_token/', UserByTokenView.as_view()),
]