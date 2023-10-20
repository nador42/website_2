from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "published",
        "date",
        "author",
        "word_count",
    )
    empty_value_display="inconnu"
    list_editable = ("published",)
    list_display_links = ("date",)
    search_fields=("title","date",)
    #list_filter = ("published","author",)
    autocomplete_fields = ("author",)
    list_per_page = 3