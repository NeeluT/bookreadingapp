from django.contrib import admin
from .models import Child, Book, Review

# Register your models here.
admin.site.register(Child)
admin.site.register(Book)
admin.site.register(Review)