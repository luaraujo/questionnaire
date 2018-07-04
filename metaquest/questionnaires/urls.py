from django.urls import path

from metaquest.questionnaires.views import (
    # questionnaire_list_view,
    # questionnaire_redirect_view,
    # questionnaire_update_view,
    questionnaire_detail_view,
)

app_name = "questionnaires"
urlpatterns = [
    # path("", view=questionnaire_list_view, name="list"),
    # path("~update/", view=questionnaire_update_view, name="update"),
    # path("<str:id>/", view=questionnaire_detail_view, name="detail"),
]
	