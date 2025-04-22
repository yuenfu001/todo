from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50,help_text="Enter Todo title")
    description = models.TextField(help_text="Enter Description")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title} {self.date_modified}"