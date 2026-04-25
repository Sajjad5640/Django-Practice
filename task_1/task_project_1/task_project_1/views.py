from django.http import HttpResponse

def dashboard_page(request):
    return HttpResponse("DashBoard is Here")
def profile_page(request):
    return HttpResponse("Profile is Here")