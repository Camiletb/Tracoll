from django.shortcuts import render

# Create your views here.

from .models import Text, Author
from django.contrib.auth.mixins import LoginRequiredMixin
def index(request):

    # Generate counts of some of the main objects
    num_texts = Text.objects.all().count()
    num_authors = Author.objects.all().count()

    ctx = {
        'num_texts': num_texts,
        'num_authors': num_authors,
	}

    # Render the template index.html with the data in the ctx variable
    return render(request, 'index.html', context=ctx)

from django.views import generic

# Para la paginación de las listas de textos y autores
class TextListView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Text
    paginate_by = 5
     
class AuthorListView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Author
    paginate_by = 5

# Para las dáginas de detalles de textos y autores
class TextDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = Text
class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = Author