from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    list_display_links = ('slug',)
    search_fields = ('name',)
    empty_value_display = 'Пусто'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    list_display_links = ('slug',)
    search_fields = ('name',)
    empty_value_display = 'Пусто'


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'category', 'description')
    list_display_links = ('category',)
    search_fields = ('name', 'category')
    empty_value_display = 'Пусто'


class ReviewyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'text', 'score', 'pub_date',)
    search_fields = ('author', 'title', 'pub_date',)
    list_filter = ('pub_date', 'author')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'text', 'review', 'pub_date',)
    search_fields = ('author', 'review', 'pub_date',)
    list_filter = ('pub_date', 'author')
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewyAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Comment, CommentAdmin)
