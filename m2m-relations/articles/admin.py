from django.contrib import admin

from .models import Article, Scope, ArticleScope


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'published_at']
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
