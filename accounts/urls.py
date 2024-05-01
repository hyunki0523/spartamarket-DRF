from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenBlacklistView
from . import views
urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("logout/", TokenBlacklistView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('signup/', views.UserCreate.as_view()),
    path("<int:pk>", views.profileAPIView.as_view(), name="profile"),

]