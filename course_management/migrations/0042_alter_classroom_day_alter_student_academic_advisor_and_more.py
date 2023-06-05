# Generated by Django 4.2 on 2023-05-21 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0041_alter_classroom_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='day',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday')], max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='academic_advisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_management.personal'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_no',
            field=models.CharField(default='0000023517', max_length=10, unique=True),
        ),
    ]
