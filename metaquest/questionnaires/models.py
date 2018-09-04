from django.db import models
from metaquest.commons.models import BaseModel

class Questionnaire(BaseModel):
	description = models.CharField(max_length=255)
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse("questionnaire-edit", kwargs={'pk': self.pk})