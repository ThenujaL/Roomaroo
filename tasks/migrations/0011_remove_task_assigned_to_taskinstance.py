# Generated by Django 4.2.4 on 2023-09-10 01:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0010_task_assigned_to_alter_house_admin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.CreateModel(
            name='TaskInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('target_dateTime', models.DateTimeField()),
                ('status', models.CharField(choices=[('DONE', 'Done'), ('TO DO', 'To do')], default='DONE', max_length=32)),
                ('assigned_to', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('parent_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
