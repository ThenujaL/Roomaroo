# Generated by Django 4.2.4 on 2023-09-10 00:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_task_house_alter_house_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('task', models.ManyToManyField(to='tasks.task')),
            ],
        ),
    ]