from django.db import models

# Create your models here.
 
class mariageT(models.Model):
    dishname = models.CharField(max_length=30)

    def __str__(self):
        return self.dishname
class mariageL(models.Model):
    dishname = models.CharField(max_length=30)

    def __str__(self):
        return self.dishname
class mariageS(models.Model):
    dishname = models.CharField(max_length=30)

    def __str__(self):
        return self.dishname
class mariageD(models.Model):
    dishname = models.CharField(max_length=30)

    def __str__(self):
        return self.dishname
class mariage2T(models.Model):
    dishname = models.CharField(max_length=30)

    def __str__(self):
        return self.dishname
class mariage2L(models.Model):
    dishname = models.CharField(max_length=30)

    def __str__(self):
        return self.dishname
class mariage2S(models.Model):
    dishname = models.CharField(max_length=30)

    def __str__(self):
        return self.dishname
class mariage2D(models.Model):
    dishname = models.CharField(max_length=30)

    def __str__(self):
        return self.dishname
class kattu(models.Model):
    dishname = models.CharField(max_length=30)

    def __str__(self):
        return self.dishname
class mariage3L(models.Model):
    dishname = models.CharField(max_length=30)

    def __str__(self):
        return self.dishname
class vira(models.Model):
    dishname = models.CharField(max_length=30)

    def __str__(self):
        return self.dishname