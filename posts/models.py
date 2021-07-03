from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]