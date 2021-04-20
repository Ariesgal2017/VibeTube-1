from django.urls import path
from vibe_auth.views import logout_view, login_page

urlpatterns = [
    path('logout', logout_view, name='logout'),
    path('accounts/login/', login_page, name="login_page")
]