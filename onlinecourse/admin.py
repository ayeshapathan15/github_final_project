from django.contrib import admin
from .models import Question, Choice, Submission

# Inline for Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

# Question admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Register models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)