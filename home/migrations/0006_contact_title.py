# Generated by Django 3.1.2 on 2020-10-24 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201024_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='title',
            field=models.CharField(default='My article', max_length=100),
        ),
    ]
