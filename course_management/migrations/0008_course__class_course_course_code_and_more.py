# Generated by Django 4.2 on 2023-04-19 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0007_alter_student_student_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='_class',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='course_code',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_no',
            field=models.CharField(default='0000002343', max_length=10, unique=True),
        ),
    ]
