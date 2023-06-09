from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /blog/5/
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
]
