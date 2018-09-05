from django.db import models
from metaquest.commons.models import BaseModel
from metaquest.questionnaires.models import Questionnaire

class Topic(BaseModel):
	questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
	description = models.CharField(max_length=255)
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.description