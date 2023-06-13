from django.shortcuts import render

# Create your views here.

from .models import Text, Author

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

class TextListView(generic.ListView):
     model = Text
     paginate_by = 3
     
class AuthorListView(generic.ListView):
     model = Author
     paginate_by = 3

