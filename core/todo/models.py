from django.db import models
from accounts.models import User

# Create your models here.

class Task(models.Model):
    """
        Represent a model of task
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    