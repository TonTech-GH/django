from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunc(request):
    '''
    Helloworldを表示する
    '''
    return_obj = HttpResponse('<h1>Hello World</h1>')

    # 追加処理
    print('response obj:', return_obj)

    return return_obj

class HelloworldView(TemplateView):
    # どのhtmlテンプテートを使うかを指定
    template_name = 'hello.html'
