from django.contrib import admin
from .models import Student,Course,Marks

# Register your models here.
admin.site.register(Student)
admin.site.register(Marks)
admin.site.register(Course)
