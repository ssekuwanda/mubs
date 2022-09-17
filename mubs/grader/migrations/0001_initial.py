# Generated by Django 4.1.1 on 2022-09-16 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4500)),
                ('years', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course_grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4500)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=255, unique=True)),
                ('surname', models.CharField(max_length=255)),
                ('other_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=6)),
                ('campus', models.CharField(max_length=45)),
                ('nationality', models.CharField(max_length=45)),
                ('program', models.CharField(max_length=45)),
                ('intake', models.CharField(max_length=45)),
                ('accyr_of_entry', models.CharField(max_length=45)),
                ('dob', models.CharField(max_length=45)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grader.course')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4500)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grader.student')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4500)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grader.year')),
            ],
        ),
        migrations.CreateModel(
            name='Course_unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4500)),
                ('code', models.CharField(max_length=4500)),
                ('credit_unit', models.CharField(max_length=4500)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grader.course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grader.semester')),
            ],
        ),
    ]