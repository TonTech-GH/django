from django.http import HttpResponse

def Helloworld(request):
    '''
    Helloworldを表示する
    '''
    return_obj = HttpResponse('<h1>Hello World</h1>')
    return return_obj
