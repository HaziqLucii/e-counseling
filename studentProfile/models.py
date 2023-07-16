from django.db import models
from student.models import Student


# CHOICES SECTION
ACHIEVEMENT_CHOICES = (
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor'),
)

MERIT_CHOICES = (
    ('5', '5'),
    ('10', '10'),
    ('15', '15'),
)

GRADE_NAME = (
    ('A+', 'A+'),
    ('A', 'A'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B', 'B'),
    ('C+', 'C+'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('G', 'G'),
)

GRADE_SCORE = (
    ('90', '90'),
    ('80', '80'),
    ('75', '75'),
    ('70', '70'),
    ('66', '66'),
    ('60', '60'),
    ('50', '50'),
    ('46', '46'),
    ('40', '40'),
    ('20', '20'),
)


# SECTION ACHIEVEMENT 
class Achievement(models.Model):
    achivementName = models.CharField(max_length=255, verbose_name="Achievement Name")
    achivementType = models.CharField(max_length=255, choices=ACHIEVEMENT_CHOICES)
    meritType = models.CharField(max_length=255, choices=MERIT_CHOICES)

    def __str__(self):
        return self.achivementName 

class StudentAchievement(models.Model):
    studentID = models.ForeignKey(Student, on_delete=models.DO_NOTHING, null=True)
    studentMerit = models.ForeignKey(Achievement, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.studentMerit


# SECTION INSTITUTE
class Institute(models.Model):
    instituteName = models.CharField(max_length=255, verbose_name="Institute Name")
    instituteDescription = models.TextField(verbose_name="Institute Description")
    instituteLink = models.URLField(verbose_name="Institute Link")

    def __str__(self):
        return self.instituteName


# SECTION PROGRAM
class Subject(models.Model):
    subjectName = models.CharField(max_length=255, verbose_name="Subject Name")

    def __str__(self):
        return self.subjectName

class Grade(models.Model):
    gradeName = models.CharField(choices=GRADE_NAME, max_length=2, verbose_name="Grade Name")
    gradeScore = models.CharField(choices=GRADE_SCORE, max_length=2, verbose_name="Score")

    def __str__(self):
        return self.gradeName

class Program(models.Model):
    programName = models.CharField(max_length=255, verbose_name="Program Name")
    programDescription = models.TextField(verbose_name="Description")
    programSubject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=True, verbose_name="Subject Required")
    programGrade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING, null=True, verbose_name="Grade Minimum Requirement")
    programInstitute = models.ForeignKey(Institute, on_delete=models.DO_NOTHING, null=True, verbose_name="Institute")

    def __str__(self):
        return self.programName


# STUDENT GRADE
class StudentGrades(models.Model):
    studentID = models.ForeignKey(Student, on_delete=models.DO_NOTHING, null=True)
    studentSubject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=True, verbose_name="Subject")
    studentGrade = models.CharField(choices=GRADE_SCORE, max_length=2, verbose_name="Score")

    def check_eligibility(self):
        eligible_programs = []  # List to store eligible programs
        
        for program in Program.objects.filter(programSubject=self.studentSubject, programGrade__gradeScore__lte=self.studentGrade):
            eligible_programs.append(program)
        
        if eligible_programs:
            program_names = [program.programName for program in eligible_programs]
            program_list = ", ".join(program_names)
            return f"{self.studentSubject}: {program_list}"
        
        return f"{self.studentSubject}: tiada"