from django.urls import path
from galeria.views import index, showImage

urlpatterns = [
    path('', index),
    path('imagem/', showImage, name='imagem'),
]
