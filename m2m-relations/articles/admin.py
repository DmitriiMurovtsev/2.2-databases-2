from django.contrib import admin
from django.forms import BaseInlineFormSet
from rest_framework.exceptions import ValidationError

from .models import Article, Scope, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        if [form.cleaned_data.get('is_main') for form in self.forms].count(True) == 0:
            raise ValidationError('Выберите основной раздел')
        if [form.cleaned_data.get('is_main') for form in self.forms].count(True) > 1:
            raise ValidationError('Основной раздел должен быть один')

        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'published_at']
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
