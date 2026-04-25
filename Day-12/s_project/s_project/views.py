from django.shortcuts import render

def home_page(req):
    context = {
        "name" : "Sajjad",
        "age" : 30,
        "adress" : "19/1A, Sher-E-Bangla Road, Hazaribagh, Dhaka"
    }
    return render(req, 'home.html',  context )
def about_page(req):
    context = {
        "name" : "Sajjad",
        "age" : 30,
        "adress" : "19/1A, Sher-E-Bangla Road, Hazaribagh, Dhaka"
    }
    return render(req, 'about.html',  context )