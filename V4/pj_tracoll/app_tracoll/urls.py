from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.index, name='index'),
    # path('logout/', views.logout_view, name='logout'),
    path('texts/', views.TextListView.as_view(), name='texts'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('text/<int:pk>', views.TextDetailView.as_view(), name='text-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('translated_texts/', views.AllTranslatedTextsListView.as_view(), name='all-translated-texts'),
    ]