from django.db import models

# Create your models here.


class Songs(models.Model):
    lyrics=models.CharField(max_length=30)
    language=models.CharField(max_length=30)
    relyear=models.IntegerField()




    class Meta:
        db_table='song'

    def __str__(self):
        return self.lyrics


class Singers(models.Model):
    sname=models.CharField(max_length=30)
    sage=models.IntegerField()
    stotalsong=models.IntegerField()

    songs= models.ManyToManyField(Songs, null=True, related_name="singers")
    class Meta:
        db_table='singer'


    def __str__(self):
        return  self.sname

class Writers(models.Model):
    wname=models.CharField(max_length=30)
    wlanguage=models.CharField(max_length=50)

    songs = models.ForeignKey(Songs, on_delete=models.CASCADE, blank=True, related_name="writers", null=True)

    class Meta:
        db_table='writer'

    def __str__(self):
        return self.wname


