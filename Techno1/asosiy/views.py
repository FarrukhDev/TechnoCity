from django.shortcuts import render, redirect
from django.views import View

from asosiy.models import Buyurtma


class Home(View):
    def get(self,request):
        return render(request,'home.html')

class About(View):
    def get(self,request):
        return render(request,'about.html')

class Contact(View):
    def get(self,request):
        return render(request,'contact.html')
    def post(self,request):
        Buyurtma.objects.create(
            fi = request.POST['ism_fam'],
            boyi = request.POST['boyi'],
            eni = request.POST['eni'],
            tel_raqam = request.POST['tel_raqam'],
            qoshimcha = request.POST['qoshimcha']
        )
        return redirect('muva')

class Shop(View):
    def get(self,request):
        return render(request,'shop.html')

class Team(View):
    def get(self,request):
        return render(request,'team.html')

class Blog(View):
    def get(self,request):
        return render(request,'blog.html')

class Muvaffaqiyat(View):
    def get(self,request):
        return render(request,'button.html')
