from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    # description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    # created_at
    # modified_at

    def __str__(self):
        return self.title