from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class UserContact(models.Model):
    email = models.EmailField(max_length=40, verbose_name="email")

class MessageContact(models.Model):
    email = models.EmailField(max_length=40, verbose_name="email")
    message = models.TextField(verbose_name="message")
    date = models.DateTimeField(verbose_name="date",null="TRUE")
    class Meta :
        ordering = ['date']
    def __str__(self):
        return f"{self.email}"


