from django.contrib import admin
from home.models import Client
from home.models import Library
from home.models import Book
from home.models import Seminar_room
from home.models import Seminar_use
from home.models import Staff
# Register your models here.
admin.site.register(Client)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Seminar_room)
admin.site.register(Seminar_use)
admin.site.register(Staff)
