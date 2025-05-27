from django.contrib import admin
from .models import Genre, Book, BookImage


class BookImageInline(admin.TabularInline):
    model = BookImage
    extra = 1
    

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active',)
    

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'owner', 'is_available')
    list_filter = ('genre', 'is_available')
    search_fields = ('title', 'author')
    inlines = [BookImageInline]
    prepopulated_fields = {'slug': ('title',)}