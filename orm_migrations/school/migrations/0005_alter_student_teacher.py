# Generated by Django 4.0.4 on 2022-05-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_student_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(to='school.teacher', verbose_name='students'),
        ),
    ]
