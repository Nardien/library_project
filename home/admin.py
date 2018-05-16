from django.contrib import admin
from home.models import Client
from home.models import Library
from home.models import Book
from home.models import SeminarRoom
from home.models import SeminarUse
from home.models import Staff
# Register your models here.
admin.site.register(Client)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(SeminarRoom)
admin.site.register(SeminarUse)
admin.site.register(Staff)
