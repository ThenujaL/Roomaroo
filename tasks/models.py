from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class House(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1000)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='house_admin')
    members = models.ManyToManyField(User, related_name='house_members')

    def __str__(self) -> str:
        return self.name
    
class Tag(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class Task(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=2000, default='', blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    house = models.ForeignKey(House, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="task_created_by")


    def __str__(self) -> str:
        return self.title


class TaskInstance(models.Model):
   DONE = "DONE"
   TODO = "TO DO"

   STATUS_CHOICES = (
       (DONE, "Done"),
       (TODO, "To do"),
   )

   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   parent_task = models.ForeignKey(Task, null=False, on_delete=models.CASCADE)
   target_dateTime = models.DateTimeField(null=False)
   status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=TODO)
   completed_image = models.ImageField(null=True, blank=True,default='default.jpg')
   assigned_to = models.ManyToManyField(User)

   def __str__(self) -> str:
       parent_taskName = self.parent_task.title
       return f'{parent_taskName} - {str(self.target_dateTime)} - {self.status}'