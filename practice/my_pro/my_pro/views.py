from django.shortcuts import render

def home_page(req):

    context = {
        "name" : "Sajjad",
        "adress" : "Chandpur",
    }
    return render(req, 'home.html', context)
def about_page(req):

    context = {
        "name" : "Sajjad",
        "adress" : "Chandpur",
    }
    return render(req, 'about.html', context)
def contact_page(req):

    context = {
        "name" : "Sajjad",
        "adress" : "Chandpur",
    }
    return render(req, 'contact.html', context)