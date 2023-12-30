from django.urls import path
from accounts.views import login_page,register_page  # 'account' modülünden 'views' modülünü ithal et

urlpatterns = [
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
]