from django.urls import path
from recipes.views import home ,sobre , cont

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', cont)
]