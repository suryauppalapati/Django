from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS =  (
        ( 'Pending', 'Pending'),
        ('completed','completed')
    )
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True,  null=True)

    def __str__(self):
        return self.title