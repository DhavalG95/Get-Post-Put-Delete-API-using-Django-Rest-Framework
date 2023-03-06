from django.db import models
import datetime



# Create your models here.


class Client(models.Model):
    client_name = models.CharField(max_length=50)
    created_at = models.DateField(default=datetime.date.today)
    created_by = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    # client = models.ForeignKey("Client",on_delete=models.CASCADE)
    client = models.CharField(max_length=50)
    created_at = models.DateField(default=datetime.date.today)
    created_by = models.CharField(max_length=50)


    def __str__(self):
        return self.project_name
    