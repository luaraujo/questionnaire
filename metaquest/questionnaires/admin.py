from django.contrib import admin

from metaquest.questionnaires.models import Questionnaire
from metaquest.questionnaires.models import Topic

admin.site.register(Questionnaire)
admin.site.register(Topic)