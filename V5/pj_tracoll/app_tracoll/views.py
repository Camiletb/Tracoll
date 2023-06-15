from django.shortcuts import render

# Create your views here.

from .models import Text, Author
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> index >>>>>>>>>>>>>>>>>>>>>>>>>>
def index(request):

    # Generate counts of some of the main objects
    num_texts   = Text.objects.all().count()
    num_authors = Author.objects.all().count()
    num_visits  =  request.session.get('num_visits', 0)
    num_visits = num_visits + 1
    request.session['num_visits'] = num_visits
    request.session.modified = True
    
    ctx = {
        'num_texts': num_texts,
        'num_authors': num_authors,
        'num_visits': num_visits,
	}

    # Render the template index.html with the data in the ctx variable
    return render(request, 'index.html', context=ctx)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> lists >>>>>>>>>>>>>>>>>>>>>>>>>>
# Para la paginación de las listas de textos y autores
class TextListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Text
    paginate_by = 5
    permission_required = 'app_tracoll.all_texts'

class AuthorListView(generic.ListView):
    #login_url = '/accounts/login/'
    model = Author
    paginate_by = 5

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> details >>>>>>>>>>>>>>>>>>>>>>>>
# Para las dáginas de detalles de textos y autores
class TextDetailView(generic.DetailView):
    # login_url = '/accounts/login/'
    model = Text
    
class AuthorDetailView(generic.DetailView):
    #login_url = '/accounts/login/'
    model = Author
    # permission_required = 'app_tracoll.all_texts'

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> permissions >>>>>>>>>>>>>>>>>>>>
class AllTranslatedTextsListView (generic.ListView):
    #login_url = '/accounts/login/'
    model = Text
    # permission_required = 'app_tracoll.is_translated'
    template_name = 'app_tracoll/text_list_translated.html'
    paginate_by = 10
    def get_queryset(self):
        all_l = Text.objects.filter(status__in=['L', 'E', 'V'])
        #all_l = Text.objects.filter(status__exact='V')
        return all_l.order_by('title')
    

# from django.contrib.auth import logout
# from django.shortcuts import redirect

# def logout_view(request):
#     logout(request)
#     return redirect('')
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Text
from .forms import TranslationForm

@login_required
@permission_required('app_tracoll.all_texts', raise_exception = True)
def edit_translation(request, text_id):
    text = get_object_or_404(Text, id=text_id)
    translation = text.get_translation()

    if request.method == 'POST':
        form = TranslationForm(request.POST, instance=translation)
        if form.is_valid():
            translation = form.save(commit=False)
            translation.original_text = text
            translation.user_translator = request.user
            translation.save()

            # Actualiza el estado del texto si no tenía traducción previa
            if text.isnot_translated:
                text.status = Text.NOT_REVIEWED
                text.save()
            # elif not text.is_marked_as_finished:
            #     text.status = Text.NOT_REVIEWED
            #     text.save()

            return HttpResponseRedirect(reverse('texts'))  # Redirige a la lista de textos después de guardar

    else:
        form = TranslationForm(instance=translation)

    return render(request, 'app_tracoll/edit_translation.html', {'form': form, 'text': text})