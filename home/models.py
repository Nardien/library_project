from django.db import models
from django.utils import timezone
# Create your models here.

class Book(models.Model):
    code = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=50)
    genre = models.CharField(max_length=3, choices = (
        ('phi', 'philosophy'),
        ('soc', 'social'),
        ('nat', 'nature'),
        ('eng', 'english'),
        ('lan', 'language')
    ))
    due = models.DateTimeField('Due Date')
    cid = models.ForeignKey(Client)
    lname = models.ForeignKey(Library)

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=15, primary_key=True)
    location = models.CharField(max_length=10)

class Client(models.Model):
    cid = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=15)
    c_type = models.CharField(max_length=4, choices = (
        ('prof', 'professor'),
        ('stud', 'student')
    ))

class Seminar_use(models.Model):
    cid = models.ManyToManyField(Client, through='Seminar_room')
    rname = models.ForeignKey(Seminar_room)
    date = models.DateTimeField(auto_now_add=True)

class Seminar_room(models.Model):
    room_name = models.CharField(max_length=10, primary_key=True)
    lname = models.ForeignKey(Library)
    available_num = models.IntegerField()

class Staff(models.Model):
    sid = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=15)
    s_type = model.CharField(max_length=8, choices = (
        ('lib', 'librarian'),
        ('room_adm', 'room_administrator'),
        ('adm', 'administrator')
    ))
    phone_n = models.CharField(max_length=4)
    lname = models.ForeignKey(Library)
