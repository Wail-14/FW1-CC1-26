from django.shortcuts import render, get_object_or_404, redirect
from collec_management.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import CollecForm
from .models import Collec
from datetime import date
from django.urls import reverse

def about(request):
    return render(request, 'about.html') 

def collection(request, n):
        collection = Collec.objects.get(pk=n)
        return render(request, 'collection.html', {'collection': collection})

def colleclist(request):
    collecs = Collec.objects.all()
    context = {"all_collec":collecs}
    return render(request,"collec_list.html",context)

def colleclist(request):
    collecs = Collec.objects.all()
    context = {"all_collec":collecs}
    return render(request,"collec_list.html",context)

def new_collec(request):
    if request.method == 'POST':
        form = CollecForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.date = date.today()
            collection.save()
            return HttpResponseRedirect(reverse('colleclist'))
    else:
        form = CollecForm()
    return render(request, 'new_collec.html', {'form': form})

def delete_collec(request, n):
    collec = get_object_or_404(Collec, pk=n)
    if request.method == "POST":
        collec.delete()
        return redirect('colleclist')
    return render(request, 'delete_collec.html', {'collec': collec})

def edit_collec(request, n):
    collec = get_object_or_404(Collec, id=n)

    if request.method == "POST":
        form = CollecForm(request.POST, instance=collec)
        if form.is_valid():
            form.save()
            return redirect('colleclist')
    else:
        form = CollecForm(instance=collec)
    return render(request, 'edit_collec.html', {'form': form, 'collec': collec})