from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class Slider(models.Model):
    image = models.ImageField(upload_to="sliders_images/%Y/%m/%d", blank=False)
    offer = models.CharField(max_length=50)
    feature = models.CharField(max_length=50)

    def __str__(self):
        return self.feature
