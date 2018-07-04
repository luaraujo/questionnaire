from django.apps import AppConfig


class QuestionnairesConfig(AppConfig):
	name = "metaquest.questionnaires"
	verbose_name = "Questionnaire"

	def ready(self):
		try:
			import questionnaires.signals  # noqa F401
		except ImportError:
			pass
