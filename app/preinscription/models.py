from django.db import models

# Create your models here.
class Preinscription(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

  def __str__ (self):
    return f'{self.name} - {self.email}'