# Generated by Django 4.2 on 2023-04-22 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0020_rename_coruse_topics_course_course_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetopic',
            name='week_no',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14')], unique=True),
        ),
    ]
