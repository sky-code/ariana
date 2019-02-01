import uuid

from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.db import models
from rest_framework.generics import get_object_or_404
from treebeard.mp_tree import MP_Node


class QuestionsAnswers(MP_Node):
    title = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self._validate_max_answers_count()

    def _validate_max_answers_count(self):
        # The number of answers associated with a question is limited to 5
        max_answers_count = settings.MAX_ANSWERS_COUNT
        parent = self.get_parent()
        if parent is not None:
            if parent.get_children_count() > max_answers_count:
                raise ValidationError(
                    f'The number of answers associated with a question is limited to {max_answers_count}')
        if self.get_children_count() > max_answers_count:
            raise ValidationError(
                f'The number of answers associated with a question is limited to {max_answers_count}')

    def __str__(self):
        return self.title


class QuestionnaireManager(models.Manager):
    def valid_qa_tree(self):
        return self.filter(is_valid_qa_tree=True)


class Questionnaire(models.Model):
    name = models.CharField(max_length=128)

    first_qa = models.ForeignKey(QuestionsAnswers, models.DO_NOTHING)

    is_valid_qa_tree = models.BooleanField(default=False)

    objects = QuestionnaireManager()

    def validate_qa_tree(self):
        # TODO implement validation of qa tree
        self.is_valid_qa_tree = True

    def save(self, *args, **kwargs):
        self.validate_qa_tree()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class QuestionnaireSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    questionnaire = models.ForeignKey(Questionnaire, models.CASCADE)

    answers = JSONField()

    finished = models.BooleanField(default=False)

    def next_questions_answers(self):
        if not len(self.answers):
            # load first answer
            questions_answers = self.questionnaire.first_qa
        else:
            last_answer = self.last_answer()
            questions_answers = last_answer.get_first_child()
        return questions_answers

    def last_answer(self):
        last_answer_id = self.answers[-1]
        last_answer = get_object_or_404(QuestionsAnswers.objects, pk=last_answer_id)
        return last_answer

    def is_valid_answer(self, answer):
        if self.finished:
            return False
        if not len(self.answers):
            return self.questionnaire.first_qa.get_children().filter(pk=answer.pk).exists()
        return self.last_answer().get_first_child().get_children().filter(pk=answer.pk).exists()

    @classmethod
    def new_questionnaire_session(cls, questionnaire_id):
        questionnaire = get_object_or_404(Questionnaire.objects.valid_qa_tree(), pk=questionnaire_id)
        qs = QuestionnaireSession.objects.create(questionnaire=questionnaire, answers=[])
        return qs.id

    def _update_finished(self):
        prev_finished = self.finished
        if len(self.answers) and not self.finished:
            last_answer = self.last_answer()
            self.finished = last_answer.get_first_child().get_children_count() == 0
            if not prev_finished and self.finished:
                self._print_answers_log()

    def save(self, *args, **kwargs):
        self._update_finished()
        super().save(*args, **kwargs)

    def _print_answers_log(self):
        msg = f'{self.questionnaire.first_qa.title}: '
        answers = []
        for answer_id in self.answers:
            answer = QuestionsAnswers.objects.get(pk=answer_id)
            answers.append(answer.title)
        msg += ' -> '.join(answers)
        print(msg)
