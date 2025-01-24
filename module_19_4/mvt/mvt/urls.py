"""
URL configuration for mvt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task1.views import shop_games_task4, games_task4, cart_task4, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop_games_task4),
    path('games/', games_task4),
    path('cart/', cart_task4),
    path('registration/', sign_up_by_django),
]
