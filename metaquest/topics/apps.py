from django.apps import AppConfig


class TopicsConfig(AppConfig):
	name = "metaquest.topics"
	verbose_name = "Topic"

	def ready(self):
		try:
			import topics.signals  # noqa F401
		except ImportError:
			pass
