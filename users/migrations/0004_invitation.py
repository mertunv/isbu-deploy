# Generated by Django 3.1.7 on 2021-05-24 18:06

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20210517_1908'),
        ('users', '0003_auto_20210517_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', ckeditor.fields.RichTextField(blank=True)),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('unread', models.BooleanField(default=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitation', to='jobs.jobs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
