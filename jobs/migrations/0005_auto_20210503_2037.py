# Generated by Django 3.1.7 on 2021-05-03 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20210503_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='type',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]