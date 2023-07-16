from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("result", views.result, name="result"),
    path("suscribe", views.suscribe, name="suscribe"),
    path("news", views.mynews),
    path("ndetails", views.ndetails),
    # path('social_links', views.social_links),
]
