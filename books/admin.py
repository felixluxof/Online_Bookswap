from django.contrib import admin
from .models import Category, Books, BookImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ('name',)


class BookImageInline(admin.TabularInline):
    model = BookImage
    extra = 1


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'owner', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description', 'owner__username')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    inlines = [BookImageInline]


@admin.register(BookImage)
class BookImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'photo')
    search_fields = ('product__name',)
