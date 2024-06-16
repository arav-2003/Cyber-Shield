from django.urls import path
from .views import signup, login,success

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('success', success , name = 'success'),
    path('login/', login, name='login'),
]