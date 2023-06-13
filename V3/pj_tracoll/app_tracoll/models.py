from django.db import models

# Create your models here.

class TextType(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the text typology: poem, song..." )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
class AuthorType(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the author type: poet, singer, band..." )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the language")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
class Author(models.Model):

    POET = 'PO'
    SINGER = 'SI'
    BAND = 'BA'

    type_choices = [
        (POET, 'Poet'),
        (SINGER, 'Singer'),
        (BAND, 'Band'),
    ]

    #type = models.CharField(max_length=2, choices=type_choices, default=SINGER)
    type = models.ForeignKey(AuthorType, on_delete=models.SET_NULL, null=True, blank=True, help_text="Enter the type of author")
    name = models.CharField(max_length=100,  help_text="Enter the name of author")
    
    class Meta:
        ordering = ['name']

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

    #type = models.CharField(max_length=2, choices=type_choices, default=SONG)
    #language = models.CharField(max_length=2, choices=language_choices)
    type = models.ForeignKey(TextType, on_delete=models.SET_NULL, null=True, blank=True, help_text="Enter the type of text")
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True, help_text="Enter the original language")
    title = models.CharField(max_length=100, help_text="Enter the title [Max. 100 letters]")
    content = models.TextField(max_length=2000, help_text="Enter the text you want translate [Max. 2000 letters]")
    state = models.CharField(max_length=1, choices=state_choices, default=NOT_TRANSLATED, help_text="Enter the translation state")

    #author = models.ForeignKey(Author, blank=True, null = True, on_delete = models.SET_NULL)
    authors = models.ManyToManyField(Author, blank=True)
    class Meta:
        ordering = ['title']

    def author(self): 
        #tengo que hacer estos getters para poder acceder a estas variables que no son propias cuando trabajo con los inlines
        return ", ".join([author.name for author in self.authors.all()])

    def __str__(self):
        print_authors = ", ".join([author.name for author in self.authors.all()])
        return f'{self.title}, {print_authors} [{self.state}]'
        #return f'{self.title}, {self.author} [{self.state}]'

import uuid  # Required for unique book instances
from datetime import date
from django.contrib.auth.models import User  # Required to assign User as a borrower

class Translation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this translation")
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    original_text = models.ForeignKey(Text, on_delete=models.RESTRICT, null=True)
    user_translator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['title', 'original_text']

    def authors(self):
        return ", ".join([author.name for author in self.original_text.authors.all()])
    
    def __str__(self):
        print_authors = ", ".join([author.name for author in self.original_text.authors.all()])
        #return f'{self.id}: {self.title}({self.original_text.title}, {print_authors})'
        return f'{self.title}, {print_authors} [from {self.original_text.language}]'
         