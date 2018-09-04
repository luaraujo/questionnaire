from django import forms


class QuestionnaireForm(forms.Form):
	description = forms.CharField(max_length=255)
	name = forms.CharField(max_length=100, unique=True)