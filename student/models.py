from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(User):
    ic = models.CharField(max_length=12, blank=False)
    namaPenuh = models.CharField(max_length=255, help_text="Sila isi nama penuh anda.")
    umur = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"