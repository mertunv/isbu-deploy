# Generated by Django 3.1.7 on 2021-05-31 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_invitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.CharField(choices=[('under_grad', 'Under Graduate'), ('bachelor', 'Bachelor'), ('high_school', 'High School'), ('doctorate', 'Doctorate')], default=None, max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, max_length=350),
        ),
        migrations.AddField(
            model_name='profile',
            name='xp',
            field=models.CharField(choices=[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9'), ('10_plus', '10+')], default=None, max_length=10),
        ),
    ]