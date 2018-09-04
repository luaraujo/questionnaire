from json import JSONEncoder
import datetime


class QuestionnaireEncoder(JSONEncoder):
	DATE_FORMAT = "%Y-%m-%d"
	TIME_FORMAT = "%H:%M:%S"
	def default(self, obj):
		if isinstance(obj, datetime.datetime):
			return obj.strftime("%s %s" % (self.DATE_FORMAT, self.TIME_FORMAT))
		return obj.__dict__ 


def json_default(value):
    if isinstance(value, datetime):
        return value.year + "-" + value.month + "-" + value.day + "-" + value.hours + "-" + value.minutes + "-" + value.seconds
    else:
        return value.__dict__