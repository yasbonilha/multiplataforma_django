from django.urls import path
from primeira_aplicacao import views

urlpatterns = [ #precisa ser exatamente esse nome ->primeiro ele passa pela url principal e depois é direcionada para essa url aqui.
    path('', views.index, name="index")
]