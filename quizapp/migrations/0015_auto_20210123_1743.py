# Generated by Django 3.0.6 on 2021-01-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0014_auto_20210123_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='link',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
    ]
