# Generated by Django 2.1.4 on 2021-02-20 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_project_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentation',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='documentation',
            field=models.ManyToManyField(blank=True, to='home.Documentation'),
        ),
    ]
