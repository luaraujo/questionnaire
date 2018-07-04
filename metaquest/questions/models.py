from django.db import models
from metaquest.commons.models import BaseModel

# Answer multiplicity choices:
# QUESTION_MULTIPLICITY_CHOICES = (
# 	('0', 'single'),
# 	('1', 'multiple'),
# 	('2', 'open_text')
# )

# class Question(BaseModel):
# 	text = models.CharField(max_length=255)
# 	order = models.PositiveSmallIntegerField()
# 	required = models.BooleanField()
# 	visible = models.CharField(max_length=255)
# 	def __str__(self):
# 		return 'Question: ' + str(self.order) + '-' + self.text