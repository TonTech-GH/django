from django.urls import path
# モジュールの中では、.を使って相対パスで読み込むモジュールを指定する
from . import views

# ここのURLパターンに応じてview等に繋ぐ
#  - path(<リクエスト>, <繋ぎ先メソッドorクラス>)
urlpatterns = [
    path('world/', views.hellofunc),
]