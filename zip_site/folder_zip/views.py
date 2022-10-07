from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, FormView

def index(request):
    return render(request,"folder_zip/home.html")