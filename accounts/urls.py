from django.urls import include, path
from accounts.views import UserCreateView

urlpatterns = [
    path('usercreate/', UserCreateView.as_view(), name='usercreate'),
]
