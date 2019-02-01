from django.urls import path

from ariana.questionnaire import views

urlpatterns = [
    path('', views.QuestionnaireList.as_view()),
    path('session/', views.QuestionnaireSessionAPIView.as_view())
]
