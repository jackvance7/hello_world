from django.urls import urls
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
