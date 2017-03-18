from django.contrib import admin
from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
    fields = ['choice_text']


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    search_fields = ['question_text']
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)

