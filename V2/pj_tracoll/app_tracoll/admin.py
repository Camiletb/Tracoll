from django.contrib import admin

# Register your models here.
from .models import Author, Text, AuthorType, TextType, Language, Translation

admin.site.register(Author)
admin.site.register(Text)
admin.site.register(AuthorType)
admin.site.register(TextType)
admin.site.register(Language)
admin.site.register(Translation)