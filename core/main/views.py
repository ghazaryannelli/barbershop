from django.shortcuts import render
from django.views.generic import ListView
from .models import HomeLogo, HomeBgInfo, HomeBG,HomeBest, HomeGet, HomeServices, HomePrice,HomeHello,HomeOur

# Create your views here.
class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homelogo = HomeLogo.objects.all()[0]
        homebginfo = HomeBgInfo.objects.all()
        homebg = HomeBG.objects.all()[0]
        homebest = HomeBest.objects.all()
        homeget = HomeGet.objects.all()
        homeservices = HomeServices.objects.all()
        homeprice = HomePrice.objects.all()
        homehello = HomeHello.objects.all()
        homeour= HomeOur.objects.all()
        return render(request, self.template_name, context={
            'homelogo':homelogo,
            'homebginfo':homebginfo,
            'homebg':homebg,
            'homebest':homebest,
            'homeget':homeget,
            'homeservices' : homeservices,
            'homeprice':homeprice,
            'homehello':homehello,
            'homeour':homeour
            })