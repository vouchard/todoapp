from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TodoItems(models.Model):
    item = models.CharField(max_length=200,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class TodoComments(models.Model):
    item = models.ForeignKey(TodoItems,on_delete=models.CASCADE)
    comment = models.CharField(max_length=200,null=False)