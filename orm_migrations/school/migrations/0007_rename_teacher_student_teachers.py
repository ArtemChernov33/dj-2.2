# Generated by Django 4.0.4 on 2022-05-12 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_alter_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
