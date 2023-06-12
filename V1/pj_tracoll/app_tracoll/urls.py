from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.index, name='index'),
    path('texts/', views.TextListView.as_view(), name='texts'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    ]