from django.http import HttpResponse
def homepage(request):
    return HttpResponse("Hello World")
def about_page(request):
    return HttpResponse("This is Aboutpage")
def contact_page(request):
    return HttpResponse("This is Contactpage")