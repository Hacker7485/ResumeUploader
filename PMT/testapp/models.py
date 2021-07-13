from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    client_name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)


class Project(models.Model):
    project_name=models.CharField(max_length=50)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
