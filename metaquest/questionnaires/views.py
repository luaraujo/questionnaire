from django.apps import apps
from django.views.generic import DetailView, ListView, UpdateView


Questionnaire = apps.get_model('Questionnaire')


class QuestionnaireDetailView(LoginRequiredMixin, DetailView):

    model = Questionnaire
    #slug_field = "username"
    #slug_url_kwarg = "username"

questionnaire_detail_view = QuestionnaireDetailView.as_view()


# class QuestionnaireListView(LoginRequiredMixin, ListView):

#     model = Questionnaire
#     #slug_field = "username"
#     #slug_url_kwarg = "username"


# questionnaire_list_view = QuestionnaireListView.as_view()


# class QuestionnaireUpdateView(LoginRequiredMixin, UpdateView):

#     model = User
#     fields = ["name"]

#     def get_success_url(self):
#         return reverse("questionnaires:detail", kwargs={"id": self.request.questionnaire.id})

#     def get_object(self):
#         return Questionnaire.objects.get(id=self.request.questionnaire.id)


# questionnaire_update_view = QuestionnaireUpdateView.as_view()

