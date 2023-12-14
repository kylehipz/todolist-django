from django.db import models


# Create your models here.
class Todo(models.Model):
    created_at = models.DateTimeField("date created")
    name = models.CharField(max_length=200)
    priority = models.CharField(
        choices=(("low", "Low"), ("high", "High")), max_length=4
    )

    def __str__(self):  # type: ignore
        return self.name
