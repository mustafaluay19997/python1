from django.db import models

# Create your models here.
class BookBaghdad(models.Model):
    Book_Name = models.CharField(max_length=150)
    Auther_Name = models.CharField(max_length=150)
    unversity_Name = models.CharField(max_length=150,default="baghdad")
    Number_page = models.IntegerField(default=0)
    date_Publish = models.DateTimeField()
    Publisher = models.CharField(max_length=150)
    Book_Pictuer = models.ImageField(upload_to="bagdad/static/bagdad/img", blank=True)
    Book_File = models.FileField(upload_to="bagdad/static/bagdad/files")