from django.http import HttpResponse




def index(request):

    return HttpResponse(request, "Hello World")





def publicwall():
    pass