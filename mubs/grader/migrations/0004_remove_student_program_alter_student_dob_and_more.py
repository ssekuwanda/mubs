# Generated by Django 4.1.1 on 2022-09-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0003_alter_academicyear_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='program',
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]
