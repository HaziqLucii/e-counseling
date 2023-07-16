from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email"]
    list_display_links = ["username"]

    add_fieldsets = (("Student Form", {"fields" : ("username", "password", "email", "ic", "namaPenuh", "umur")}), )

    fieldsets = (("Student Form", {"fields" : ("username", "password", "email", "ic", "namaPenuh", "umur")}), )

    def save_model(self, request, obj, form, change):
        # Hash the password field
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)