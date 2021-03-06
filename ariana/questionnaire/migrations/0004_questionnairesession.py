# Generated by Django 2.0.10 on 2019-01-30 20:13

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_auto_20190128_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionnaireSession',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answers', django.contrib.postgres.fields.jsonb.JSONField()),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Questionnaire')),
            ],
        ),
    ]
