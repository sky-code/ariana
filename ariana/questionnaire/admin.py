from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from ariana.questionnaire.models import QuestionsAnswers, Questionnaire


@admin.register(QuestionsAnswers)
class QuestionsAnswersAdmin(TreeAdmin):
    form = movenodeform_factory(QuestionsAnswers)


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_qa', 'is_valid_qa_tree')
