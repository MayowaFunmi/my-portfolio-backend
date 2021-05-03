from django.contrib import admin
from .models import Project, Book, ContactMe

# Register your models here.
admin.site.register(Project)
admin.site.register(Book)
admin.site.register(ContactMe)
admin.site.site_header = 'My Portfolio Website'