# Generated by Django 3.1.7 on 2021-06-05 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210604_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='number_of_children',
        ),
    ]
