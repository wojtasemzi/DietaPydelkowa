# Generated by Django 4.0.3 on 2022-03-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='tags',
            field=models.ManyToManyField(to='ingredients.tag'),
        ),
    ]
