# Generated by Django 2.0.3 on 2018-05-08 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_auto_20180508_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
    ]
