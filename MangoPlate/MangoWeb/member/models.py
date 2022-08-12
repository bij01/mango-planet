from django.db import models


class Member(models.Model):
    email = models.EmailField(max_length=60, primary_key=True)
    name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=45)
    rdate = models.DateTimeField(auto_now=True)
    
class Qna(models.Model):
    writer = models.EmailField(max_length=60)
    comment = models.TextField()
    rdate = models.DateField(auto_now=True)
