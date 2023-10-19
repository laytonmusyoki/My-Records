from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    notes=models.CharField(max_length=200,blank=True,null=True)
    date=models.DateField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.notes
