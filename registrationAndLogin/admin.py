from django.contrib import admin
from .models import University, SchoolSystem, Student
# Register your models here.
admin.site.register(SchoolSystem)
admin.site.register(University)
admin.site.register(Student)
