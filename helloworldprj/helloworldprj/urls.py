"""helloworldprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# モジュールの中では、.を使って相対パスで読み込むモジュールを指定する
# from .views import Helloworld
from . import views

# ここのURLパターンに応じてview等に繋ぐ
#  - path(<リクエスト>, <繋ぎ先メソッドorクラス>)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.helloworldfunc),
    path('hello_class/', views.HelloworldView.as_view())
]
