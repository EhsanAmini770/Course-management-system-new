# Generated by Django 4.2 on 2023-05-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0043_alter_student_student_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_document',
            field=models.FileField(null=True, upload_to='lesson_documents/'),
        ),
    ]