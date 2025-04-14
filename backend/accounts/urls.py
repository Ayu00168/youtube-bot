from django.urls import path, include
from .views import CreateUserView, LoginUserView, LogoutUserView, ChangePasswordView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]