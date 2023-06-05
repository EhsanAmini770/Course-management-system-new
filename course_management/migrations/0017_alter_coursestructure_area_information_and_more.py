# Generated by Django 4.2 on 2023-04-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0016_alter_course_course_structure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursestructure',
            name='area_information',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coursestructure',
            name='educational_science',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coursestructure',
            name='engineering_design',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coursestructure',
            name='engineering_science',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coursestructure',
            name='health_science',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coursestructure',
            name='liberal_arts',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coursestructure',
            name='math_science',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coursestructure',
            name='science',
            field=models.IntegerField(default=0),
        ),
    ]