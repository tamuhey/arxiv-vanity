# Generated by Django 2.0.9 on 2019-01-11 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0021_paper_source_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='source_file_old',
        ),
    ]
