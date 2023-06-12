from django.db import models

# Create your models here.
class Author(models.Model):

    POET = 'PO'
    SINGER = 'SI'
    BAND = 'BA'

    type_choices = [
        (POET, 'Poet'),
        (SINGER, 'Singer'),
        (BAND, 'Band'),
    ]

    type = models.CharField(max_length=2, choices=type_choices, default=SINGER)
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name', 'type']

    def __str__(self):
        return self.name
        #return f'{self.author_name}, {self.author_type}'

class Text(models.Model):

    POEM = 'PO'
    SONG = 'SO'

    NOT_TRANSLATED = 'W'
    NOT_REVIEWED = 'L'
    REVIEWED_EDITABLE = 'E'
    TOTALLY_TRANSLATED = 'W'

    ES = 'ES'
    FR = 'FR'
    EN = 'EN'
    
    
    type_choices = [
        (POEM, 'Poem'),
        (SONG, 'Song'),
    ]

    language_choices = [
        (ES, 'ES'),
        (FR, 'FR'),
        (EN, 'EN'),
    ]

    state_choices = [
        (NOT_TRANSLATED, '(W) Not translated'),
        (NOT_REVIEWED, '(L) Translated & Not reviewed'),
        (REVIEWED_EDITABLE, ' (E) Reviewed & Editable'),
        (TOTALLY_TRANSLATED, ' (V) Translated'),
    ]

    type = models.CharField(max_length=2, choices=type_choices, default=SONG)
    language = models.CharField(max_length=2, choices=language_choices)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    state = models.CharField(max_length=1, choices=state_choices, default=NOT_TRANSLATED)

    author = models.ForeignKey(Author, blank=True, null = True, on_delete = models.SET_NULL)
    #authors = models.ManyToManyField(Author, blank=True)
    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title}, {self.author} [{self.state}]'