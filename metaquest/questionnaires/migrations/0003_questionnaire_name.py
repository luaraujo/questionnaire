# Generated by Django 2.0.6 on 2018-07-07 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0002_auto_20180705_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='name',
            field=models.CharField(default='Teste', max_length=100),
        ),
    ]
