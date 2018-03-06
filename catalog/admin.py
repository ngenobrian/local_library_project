from django.contrib import admin
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.mixins import LoginRequiredMixin

# Register your models here.

# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
# admin.site.register(Genre)


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
# this is a class that enables book info and book instance to be on the same detail page
# Tabularinline(will be arranged horizontally) or StackedInline(vertically)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]  # enables bookinstance to be included in book details page

admin.site.register(Book, BookAdmin)  # this is a decorator that is the same as admin.site.register


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
    # fieldsets attribute adds sections to grup related model info within detail form
    # 'Availability' is title of the section, or u use None if u dont want a title

admin.site.register(BookInstance, BookInstanceAdmin)


class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre)





