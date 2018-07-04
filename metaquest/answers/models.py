from django.db import models
from metaquest.commons.models import BaseModel


# class SingleAnswer (BaseModel):
# 	text = models.CharField(max_length=255)
# 	size = models.PositiveSmallIntegerField()
# 	precision = models.PositiveSmallIntegerField()
# 	name = models.CharField(max_length=255)
# 	value = models.CharField(max_length=255)
# 	def __str__(self):
# 		return 'Answer: ' + str(self.order) + '-' + self.text

# class DerivatedAnswer (BaseModel):
# 	text = models.CharField(max_length=255)
# 	expression = models.CharField(max_length=255)
# 	def __str__(self):
# 		return 'DerivatedAnswer: ' + self.expression

# class MultipleAnswerSingleChoice()
# 	order = models.PositiveSmallIntegerField()
# 	type_choice = models.CharField(max_length=1, choices=ANSWER_TYPE_CHOICES)
	

# class MultipleAnswerMultipleChoice