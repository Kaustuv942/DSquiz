# Generated by Django 3.0.6 on 2021-01-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0013_auto_20210123_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
