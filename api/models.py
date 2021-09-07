from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar/default.png', upload_to="avatar")

    def __str__(self):
        return self.user.username + ' Profile'

class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(default="UntitledForm", max_length=20)
    description = models.CharField(default="", max_length=100)
    start_id = models.UUIDField(default=None, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    box = models.JSONField(default=list)

    def __str__(self):
        return self.title

    def dict(self):
        return {
            "titie": self.title,
            "description": self.description,
            "id": self.id,
            "start_id": self.start_id,
            "box": self.box,
            "date": self.date
        }

    def profile_dict(self):
        return {
            "titie": self.title,
            "description": self.description,
            "id": self.id,
            "date": self.date
        }