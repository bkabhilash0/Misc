# Generated by Django 3.1.2 on 2020-10-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default='pdf/test.pdf', upload_to='pdf/'),
        ),
    ]