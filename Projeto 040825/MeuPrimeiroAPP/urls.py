from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('areadoaluno', views.areadoaluno, name='areadoaluno'),
    path('planos', views.planos, name='planos'),
    path('sobrenos', views.sobrenos, name='sobrenos'),
    path('trabalhe', views.trabalhe, name='trabalhe'),
]