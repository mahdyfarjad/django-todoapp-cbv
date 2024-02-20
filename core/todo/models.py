from django.db import models

# Create your models here.
class Task(models.Model):
    """
        Represent a model of task
    """

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_know_add=True)

    def __str__(self) -> str:
        return self.title