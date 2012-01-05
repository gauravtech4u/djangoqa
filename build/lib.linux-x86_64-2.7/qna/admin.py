from django.contrib import admin
from models import *
from django.utils.translation import ugettext_lazy as _

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    max_num = 10
    
class QuestionnaireAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",),}
    inlines = [QuestionInline,]
    readonly_fields=('created_date',)

class QuestionChoiceInline(admin.StackedInline):
    model = QuestionChoice
    extra = 1
    max_num = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'description','type', )
    inlines = [QuestionChoiceInline,]
    readonly_fields=('created_date',)

class AnswerAdmin(admin.ModelAdmin):
    readonly_fields=('description','question',)

admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(QuestionChoice)