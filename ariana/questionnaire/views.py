# Create your views here.
from django.http import Http404
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

from ariana.questionnaire.models import Questionnaire, QuestionnaireSession, QuestionsAnswers
from ariana.questionnaire.serializers import QuestionnaireSerializer, QuestionnaireCreateSerializer, \
    QuestionnaireSessionAnswerSerializer


class QuestionnaireList(generics.ListCreateAPIView):
    queryset = Questionnaire.objects.valid_qa_tree()
    serializer_class = QuestionnaireSerializer

    def create(self, request, *args, **kwargs):
        serializer = QuestionnaireCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        questionnaire_session_id = QuestionnaireSession.new_questionnaire_session(serializer.data['id'])
        return Response({'id': questionnaire_session_id}, status=status.HTTP_201_CREATED)


class QuestionnaireSessionAPIView(GenericAPIView):
    def get(self, request, *_args, **_kwargs):
        questionnaire_session_id = request.GET.get('id', None)
        if questionnaire_session_id is None:
            raise Http404()
        qs = get_object_or_404(QuestionnaireSession.objects.select_related('questionnaire'),
                               pk=questionnaire_session_id)
        return self._qs_response(qs)

    def post(self, request, *_args, **_kwargs):
        serializer = QuestionnaireSessionAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        qs = get_object_or_404(QuestionnaireSession.objects, pk=serializer.validated_data['questionnaire_id'])
        answer = get_object_or_404(QuestionsAnswers.objects, pk=serializer.validated_data['answer_id'])
        if not qs.is_valid_answer(answer):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        qs.answers.append(answer.pk)
        qs.save()
        return self._qs_response(qs)

    def _qs_response(self, qs):
        response_data = {
            'questionnaireName': qs.questionnaire.name,
            'questionTitle': None,
            'questionAnswers': None,
            'finished': qs.finished
        }
        if qs.finished:
            last_answer_response = qs.next_questions_answers()
            response_data['questionTitle'] = last_answer_response.title
            return Response(response_data, status=status.HTTP_200_OK)
        questions_answers = qs.next_questions_answers()
        response_data['questionTitle'] = questions_answers.title
        response_data['questionAnswers'] = [{'id': qa.pk, 'title': qa.title} for qa in questions_answers.get_children()]

        return Response(response_data, status=status.HTTP_200_OK)
