from django.contrib import admin

# Register your models here.
from .models import Author, Text, AuthorType, TextType, Language, Translation

#Inlines
# class AuthorInline (admin.TabularInline): # Para añadir este campo a la página de textos
#     model = Author.name
#     #fk_name = 'author'

class TextsInline (admin.TabularInline): # Para añadir este campo a la página de textos
    extra = 0
    model = Text.authors.through #Solución distinta a la de clase para los casos de Many-to-Many

class TranslationInline (admin.TabularInline): # Para añadir este campo a la página de textos
    extra = 0
    model = Translation

#Admin classes
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'translated_texts', 'total_texts')
    fields = ['name', 'type']
    inlines = [
        TextsInline,
    ]

class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'language', 'status')
    fields = ['title', 'content', 'authors', ('type', 'language'), 'status']
    inlines = [
        TranslationInline,
    ]

class TranslationAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'original_title', 'authors', 'user_translator', 'status')
    # fieldsets = (
    #     ('Translation', {'fields': ('title', 'content')}),
    #     ('More info', {'fields': ('id')}),
    #     )
    fieldsets = (
            ('Content', {
                'fields': ('title', 'content')}),
            ('Translation info', {
                'fields': ('original_text', 'user_translator', 'id')}),
            )
admin.site.register(Author, AuthorAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(AuthorType)
admin.site.register(TextType)
admin.site.register(Language)
admin.site.register(Translation, TranslationAdmin)