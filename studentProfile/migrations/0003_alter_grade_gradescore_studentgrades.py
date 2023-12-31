# Generated by Django 4.1.7 on 2023-07-16 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('studentProfile', '0002_alter_program_programdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='gradeScore',
            field=models.CharField(choices=[('90', '90'), ('80', '80'), ('75', '75'), ('70', '70'), ('66', '66'), ('60', '60'), ('50', '50'), ('46', '46'), ('40', '40'), ('20', '20')], max_length=2, verbose_name='Score'),
        ),
        migrations.CreateModel(
            name='StudentGrades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentGrade', models.CharField(choices=[('90', '90'), ('80', '80'), ('75', '75'), ('70', '70'), ('66', '66'), ('60', '60'), ('50', '50'), ('46', '46'), ('40', '40'), ('20', '20')], max_length=2, verbose_name='Score')),
                ('studentID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student.student')),
                ('studentSubject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentProfile.subject', verbose_name='Subject')),
            ],
        ),
    ]
