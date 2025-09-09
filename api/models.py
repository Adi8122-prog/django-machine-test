from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    client = models.ForeignKey(Client, related_name="projects", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name="projects")
    created_by = models.ForeignKey(User, related_name="created_projects", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
