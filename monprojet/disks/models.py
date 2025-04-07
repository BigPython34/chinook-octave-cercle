from django.db import models

class Artist(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=255)


class Album(models.Model):
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=255)
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    
class Track(models.Model):
    id=models.AutoField(primary_key=True)  
    name = models.CharField(max_length=255)
    composer = models.CharField(max_length=255,null=True)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=10, decimal_places=3)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


