from . import views
from django.urls import path

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
