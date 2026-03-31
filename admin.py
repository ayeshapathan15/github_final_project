from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# Inline for Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


# Inline for Question
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# Register all models
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
