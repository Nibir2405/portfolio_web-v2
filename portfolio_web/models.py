from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=13)
    content = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)