# Generated by Django 3.0.5 on 2020-04-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articles_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
