# Generated by Django 2.0.1 on 2018-01-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0012_paper_arxiv_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
