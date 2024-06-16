from django.contrib import admin
from django.urls import path,include
from sub import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name = 'signup'),
    path('success/',views.success, name = 'success'),
    path('',views.welcome, name = 'welcome'),
    path('welcome/',views.welcome, name = 'welcome'),
    path('login/',views.login,name = 'login'),
    path('about/',views.about,name = 'about'),
    path('login_success/',views.login_success,name='login_success'),
]
