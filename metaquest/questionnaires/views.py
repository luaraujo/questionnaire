from metaquest.questionnaires.models import Questionnaire
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class QuestionnaireList(ListView):
    model = Questionnaire

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
    	return super(QuestionnaireList, self).dispatch(*args, **kwargs)


class QuestionnaireDetail(DetailView):
    model = Questionnaire

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
    	return super(QuestionnaireDetail, self).dispatch(*args, **kwargs)

class QuestionnaireCreate(CreateView):
    model = Questionnaire
    fields = ['name','description']

    success_url = reverse_lazy('questionnaires:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
    	return super(QuestionnaireCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
    	form.instance.created_by = self.request.user
    	return super().form_valid(form) 

class QuestionnaireUpdate(UpdateView):
    model = Questionnaire
    fields = ['description']
    success_url = reverse_lazy('questionnaires:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
    	return super(QuestionnaireUpdate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
    	form.instance.created_by = self.request.user
    	return super().form_valid(form)

class QuestionnaireDelete(DeleteView):
    model = Questionnaire
    success_url = reverse_lazy('questionnaires:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
    	return super(QuestionnaireDelete, self).dispatch(*args, **kwargs)
