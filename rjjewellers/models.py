from django.db import models

class GoldImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.title