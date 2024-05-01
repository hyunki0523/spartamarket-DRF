from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProductListAPIView.as_view()),
    path("create/", views.ProducCreateAPIView.as_view()),
    path("<int:pk>/", views.ProductDetailAPIView.as_view()),

]