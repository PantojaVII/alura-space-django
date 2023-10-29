from django.shortcuts import render


def index(request):
    return render(request,  'galeria/index.html')


def showImage(request):
    return render(request,  'galeria/imagem.html')
