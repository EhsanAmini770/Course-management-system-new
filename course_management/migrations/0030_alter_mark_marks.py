# Generated by Django 4.2 on 2023-05-19 12:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0029_alter_course_midterm_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='marks',
            field=models.IntegerField(default=None, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
