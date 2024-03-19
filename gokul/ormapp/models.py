from django.db import models
from django.contrib import admin
class Book(models.Model):
    Bookid=models.IntegerField(primary_key=True);
    Bookname=models.CharField(max_length=40);
    Author=models.CharField(max_length=20);
    published=models.DateField();
    price=models.IntegerField();
class BookAdmin(admin.ModelAdmin):
    list_display=("Bookid","Bookname","Author","published","price");

