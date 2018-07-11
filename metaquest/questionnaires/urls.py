from django.urls import path
from metaquest.questionnaires import views

from metaquest.questionnaires.models import Questionnaire

app_name = "questionnaires"
urlpatterns = [ 
	path('add_topic/', views.TopicCreate.as_view(), name="add-topic"),
	path('delete_topic/', views.TopicDelete.as_view(), name="delete-topic"),
	path('update_topic/', views.TopicUpdate.as_view(), name="update-topic"),
	path('add/', views.QuestionnaireCreate.as_view(), name="add"),
	path('update/<int:pk>/', views.QuestionnaireUpdate.as_view(), name='update'),
	path('delete/<int:pk>/', views.QuestionnaireDelete.as_view(), name='delete'),
	path('detail/<int:pk>', views.QuestionnaireDetail.as_view(), name='detail'),
	path("", views.QuestionnaireList.as_view() , name="list"),
]