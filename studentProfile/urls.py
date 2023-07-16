from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name="profile_page"),
    path('achievement/', views.studentAchievement, name="achievement_page"),
    path('student_grade/', views.StudentGrades, name="student_grade_page"),
]
