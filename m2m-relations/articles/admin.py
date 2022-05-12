from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Article, Tag, Scope
from django.forms import BaseInlineFormSet


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = False
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                if is_main:
                    raise ValidationError('Основным может быть только один раздел')
                else:
                    is_main = True
        if not is_main:
            raise ValidationError('Укажите основной раздел')
        return super().clean()



class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 5

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
