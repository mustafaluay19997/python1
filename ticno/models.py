from django.db import models

# Create your models here.
class Bookticno(models.Model):
    Book_Name = models.CharField(max_length=150)
    Auther_Name = models.CharField(max_length=150)
    unversity_Name = models.CharField(max_length=150,default="Technology")
    Number_page = models.IntegerField(default=0)
    date_Publish = models.DateTimeField()
    Publisher = models.CharField(max_length=150)
    Book_Pictuer = models.ImageField(upload_to="ticno/static/ticno/img", blank=True)
    Book_File = models.FileField(upload_to="ticno/static/ticno/files")
