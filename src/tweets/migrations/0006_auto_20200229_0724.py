# Generated by Django 3.0.3 on 2020-02-29 01:54

from django.db import migrations, models
import tweets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20200228_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=140, validators=[tweets.models.validate_content]),
        ),
    ]
