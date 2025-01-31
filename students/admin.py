from django.contrib import admin
from students.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course')  # Customize columns
    search_fields = ('name', 'email')  # Add search functionality


admin.site.register(Student, StudentAdmin)
