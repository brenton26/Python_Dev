# Generated by Django 2.2.5 on 2020-03-30 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EdsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='animal_type',
        ),
    ]
