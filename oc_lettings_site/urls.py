from django.contrib import admin
from django.urls import path

from . import views
# import the view from "lettings" app
from lettings import views as views_lettings


urlpatterns = [
    path('', views.index, name='index'),
    # redirect the url to the "lettings_index" view in "lettings" app
    path('lettings/', views_lettings.lettings_index, name='lettings_index'),
    # redirect the url to the "letting" view in "lettings" app     
    path('lettings/<int:letting_id>/', views_lettings.letting, name='letting'),
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
