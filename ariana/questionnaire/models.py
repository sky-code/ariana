from django.db import models
from treebeard.mp_tree import MP_Node


class QuestionsAnswers(MP_Node):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Questionnaire(models.Model):
    title = models.CharField(max_length=128)

    start_questions_answers = models.ForeignKey(QuestionsAnswers, models.DO_NOTHING)
