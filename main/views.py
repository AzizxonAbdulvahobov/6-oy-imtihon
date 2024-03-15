from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    home = models.Home.objects.last()
    about = models.AboutUs.objects.last()
    reklamalar = models.Reklamalar.objects.last()
    service = models.Service.objects.all()
    blog = models.Blog.objects.all()
    context = { 
        'home': home,
        'about' : about,
        'reklamalar' : reklamalar,
        'service' : service,
        'blog' : blog,
    }
    return render(request, 'index.html' , context)

def about(request):
    about = models.AboutUs.objects.last()
    context = {
        'about' : about,
    }
    return render(request, 'about.html', context)

def service(request):
    service = models.Service.objects.all()
    context = {
        'service' : service,
    }
    return render(request, 'service.html', context)

def contact(request):
    if request.method == 'POST':
        try:
            models.Xabar_qoldirish.objects.create( 
                name = request.POST['name'],
                phone = request.POST['phone'],
                email = request.POST['email'],
                message = request.POST['message']
             )
        except:
            ...
    return render(request, 'contact.html')

