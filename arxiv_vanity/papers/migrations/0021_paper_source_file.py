# Generated by Django 2.0.6 on 2018-06-21 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0020_auto_20180621_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='source_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='papers.SourceFile'),
        ),
    ]
