from django.contrib import admin
from . import models

# Achievement
@admin.register(models.Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ["achivementName", "achivementType", "meritType"]
    list_display_links = ["achivementName"]

    add_fieldsets = (("Achievement Form", {"fields" : ("achivementName", "achivementType", "meritType",)}), )

    fieldsets = (("Achievement Form", {"fields" : ("achivementName", "achivementType", "meritType",)}),)


# Institute
@admin.register(models.Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ["instituteName", "instituteDescription", "instituteLink"]
    list_display_links = ["instituteName"]

    add_fieldsets = (("Institute Form", {"fields" : ("instituteName", "instituteDescription", "instituteLink")}), )

    fieldsets = (("Institute Form", {"fields" : ("instituteName", "instituteDescription", "instituteLink")}),)


# Subject
@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["subjectName",]
    list_display_links = ["subjectName"]

    add_fieldsets = (("Subject Form", {"fields" : ("subjectName",)}), )

    fieldsets = (("Subject Form", {"fields" : ("subjectName",)}),)


# Grade
@admin.register(models.Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ["gradeName", "gradeScore"]
    list_display_links = ["gradeName"]

    add_fieldsets = (("Grade Form", {"fields" : ("gradeName", "gradeScore")}), )

    fieldsets = (("Grade Form", {"fields" : ("gradeName", "gradeScore")}),)


# Program
@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ["programName", "programDescription", "programSubject", "programGrade", "programInstitute"]
    list_display_links = ["programName"]

    add_fieldsets = (("Program Form", {"fields" : ("programName", "programDescription", "programSubject", "programGrade", "programInstitute")}), )

    fieldsets = (("Program Form", {"fields" : ("programName", "programDescription", "programSubject", "programGrade", "programInstitute")}),)


# STUDENT SECTION

# StudentAchievement
@admin.register(models.StudentAchievement)
class StudentAchievementAdmin(admin.ModelAdmin):
    list_display = ["studentID", "studentMerit"]
    list_display_links = ["studentMerit"]

    add_fieldsets = (("Student Achievement Form", {"fields" : ("studentID", "studentMerit")}), )

    fieldsets = (("Student Achievement Form", {"fields" : ("studentID", "studentMerit")}),)


# StudentAchievement
@admin.register(models.StudentGrades)
class StudentGradesAdmin(admin.ModelAdmin):
    list_display = ["studentID", "studentSubject", "studentGrade"]
    list_display_links = ["studentSubject"]

    add_fieldsets = (("Student Grade Form", {"fields" : ("studentID", "studentSubject", "studentGrade")}), )

    fieldsets = (("Student Grade Form", {"fields" : ("studentID", "studentSubject", "studentGrade")}),)