from rest_framework import serializers

from ariana.questionnaire.models import Questionnaire


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('id', 'name')


class QuestionnaireCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)


class QuestionnaireSessionAnswerSerializer(serializers.Serializer):
    questionnaire_id = serializers.CharField()
    answer_id = serializers.CharField()
