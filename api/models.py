from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forms = models.JSONField(default=list)

    def __str__(self):
        return self.user.username + ' Profile'

class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(default="UntitledForm", max_length=20)
    description = models.CharField(default="", max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    box = models.JSONField(default=list)

    def __str__(self):
        return self.title

    def dict(self):
        return {
            "titie": self.title,
            "description": self.description,
            "id": self.id,
            "box": self.box
        }