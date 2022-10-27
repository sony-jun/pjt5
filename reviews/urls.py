from django.urls import path, include
from . import views

app_name = "reviews"

urlpatterns = [
    path('', views.reviews_article, name="reviews-article"),
    path('create/', views.reviews_create, name="reviews-create"),

]
