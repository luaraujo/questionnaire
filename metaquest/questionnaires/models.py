from django.db import models
from metaquest.commons.models import BaseModel

class Questionnaire(BaseModel):
	description = models.CharField(max_length=255)

	def __str__(self):
		return self.description

class Topic(BaseModel):
	description = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	order = models.PositiveSmallIntegerField()
	image = models.ImageField()
	questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
	# Has a List of QuestionGroups

	def __str__(self):
		return 'Topic: ' + str(self.order) + '-' + self.description