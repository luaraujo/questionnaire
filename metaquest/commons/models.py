from django.db import models
from metaquest.users.models import User


class BaseModel(models.Model):

	created = models.DateTimeField("created on", auto_now_add=True)
	modified = models.DateTimeField("updated on", auto_now=True)
	help_str = models.CharField("help text to help users filling the questionnaire", max_length=255)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	class Meta:
		abstract = True