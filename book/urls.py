from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("booklist", views.PublicView.as_view(), name="booklist"),
    path("booklist/<int:pk>/", views.BookView.as_view(), name="bookDetail"),
    path("books", views.BookCreate.as_view(), name="booklist"),
    path("bookupdate/<int:pk>/", views.BookUpdate.as_view(), name="bookDetail"),
    path("register/", views.Register.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
