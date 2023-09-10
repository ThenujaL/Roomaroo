# Generated by Django 4.2.4 on 2023-09-10 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(null=True, to='tasks.tag'),
        ),
    ]