# Generated by Django 3.1.7 on 2021-05-03 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20210503_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs.type'),
        ),
    ]
