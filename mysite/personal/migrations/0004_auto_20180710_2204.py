# Generated by Django 2.0.3 on 2018-07-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_userprofile_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(default='', max_length=600),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='experience',
            field=models.TextField(default='', max_length=600),
        ),
    ]
