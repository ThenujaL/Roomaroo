from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class House(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1000)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='task_admin')
    members = models.ManyToManyField(User, related_name='task_members')

    def __str__(self) -> str:
        return self.name

class Task(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=2000, default='', blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    house = models.ForeignKey(House, null=True, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return self.title

