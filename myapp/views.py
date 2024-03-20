from django.shortcuts import render,redirect
from .models import *


def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {"categories":categories, "photos":photos}
    return render(request,"myapp/gallery.html",context)

def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {"photo":photo}
    return render(request,"myapp/photo.html",context)

def addphoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get("image")
        description = data.get("description")

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['catogery_new'] != '':
            category, created = Category.objects.get_or_create(name=data['catogery_new'])
        else:
            category = None
        Photo.objects.create(
            category = category,
            description = description,
            image = image
        )

        return redirect('gallery')

    context = {"categories":categories}
    return render(request,"myapp/add.html",context)
