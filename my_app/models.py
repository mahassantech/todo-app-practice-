from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TaskModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    