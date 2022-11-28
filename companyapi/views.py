from django.http import HttpResponse

def home_page(request):
    print('This is home page')
    return HttpResponse('This is home page.')
