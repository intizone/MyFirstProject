from django.db import models

# Create your models here.

class Portfolio(models.Model):
    sort = models.IntegerField()
    title = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='images/')


class Message(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.CharField(max_length = 255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Murojaatlar ro'yxati"
        verbose_name_plural = "Murojaatlar"
        ordering = ("id",)
    