# Generated by Django 4.2 on 2023-05-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0045_alter_course_final_exam_alter_course_midterm_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_no',
            field=models.CharField(default='0000023510', max_length=10, unique=True),
        ),
    ]
