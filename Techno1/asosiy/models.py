from django.db import models

class Buyurtma(models.Model):
    fi = models.CharField(max_length=30)
    boyi = models.CharField(max_length=10)
    eni = models.CharField(max_length=10)
    qoshimcha = models.TextField()
    tel_raqam = models.CharField(max_length=13)
    def __str__(self):
        return self.fi

class Haridor(models.Model):
    ism = models.CharField(max_length=20)
    familiya = models.CharField(max_length=20)
    tel_raqam = models.CharField(max_length=13)
    buyurtma = models.TextField()
