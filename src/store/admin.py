from django.contrib import admin
from store.models import Book


# Register your models here.
#admin.site.register(Book)

@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = (
        'title',
        'kind',
        'slug',
        'word_count',
    )

    empty_value_display = 'Unknow'

    list_editable = ('slug',)
    #list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('kind',)
    autocomplete_field = ('title',)
    list_per_page = 25