from django.db import models

# Create your models here.
class instrument(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="no descr...",null=True)

    def __str__ (self):
        return str(self.name)